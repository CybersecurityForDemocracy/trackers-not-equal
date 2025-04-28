chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'fetchFacebookData') {
        fetch(request.url)
            .then(response => response.text())
            .then(content => sendResponse({data: content}))
            .catch(error => sendResponse({error: error.toString()}));
 
    }
    return true;
});

