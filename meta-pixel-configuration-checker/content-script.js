let matchKeys = null;

function extractSelectedMatchKeys(configString) {
  const regex = /"selectedMatchKeys":\s*\[(.*?)\]/;
  const match = configString.match(regex);
  
  if (match && match[1]) {
    const keysString = match[1];
    const keys = keysString.split(',').map(key => key.trim().replace(/"/g, ''));
    return keys;
  }
  
  return null;
}

function readFacebookFile() {
    const scripts = document.querySelectorAll('script[src^="https://connect.facebook.net/signals/config/"]');

    scripts.forEach(script => {
      chrome.runtime.sendMessage({
        action: 'fetchFacebookData',
        url: script.src
      }, response => {
        if (response.data) {
          const selectedMatchKeys = extractSelectedMatchKeys(response.data);
          matchKeys = selectedMatchKeys;
          chrome.runtime.sendMessage({
            action: "matchKeys",
            data: {
              keys: selectedMatchKeys
            }
          });
        } else {
          console.error('Error:', response.error);
        }
      });
    });
    
}

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if (request.action === "getDataForPopup") {
    if (matchKeys) {
      sendResponse({data: {keys: matchKeys}});
    }
  }
});
  
// Run the function when the page is fully loaded
if (document.readyState === 'complete') {
  readFacebookFile();
} else {
  window.addEventListener('load', readFacebookFile);
}