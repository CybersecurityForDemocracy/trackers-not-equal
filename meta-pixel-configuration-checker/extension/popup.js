function mapKeyToName(key) {
    const keyMap = {
      'em': 'Email',
      'fn': 'First Name',
      'ln': 'Last Name',
      'ph': 'Phone Number',
      'ge': 'Gender',
      'ct': 'City',
      'st': 'State',
      'zp': 'Zip Code',
      'db': 'Date of Birth',
      'country': 'Country',
      'external_id': 'External ID'
    };
  
    return keyMap[key] || key;
}

function updatePopup(keyList) {
  document.getElementById('header').innerHTML = "The following data may be collected by Meta, if entered into a form:";
  document.getElementById('keys').innerHTML = keyList.map(mapKeyToName).map(item => `- ${item}`).join('<br>');
}

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    console.log("Received message: ", message);
    if (message.action === "matchKeys") {
      updatePopup(message.data.keys);
    }
});

chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
  chrome.tabs.sendMessage(tabs[0].id, {action: "getDataForPopup"}, function(response) {
    if (response && response.data) {
      updatePopup(response.data.keys);
    }
  });
});