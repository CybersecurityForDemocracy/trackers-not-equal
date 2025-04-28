## meta-pixel-configugration-checker
This is a standalone Chrome extension that will check a website for a Meta Pixel and, if that pixel is configured for automatic form data collection, display the types of PII it is configured to collect in a pop-up. 

To use:

a) Download the extension locally.

b) Navigate to chrome://extensions in Chrome.

c) Ensure developer mode is toggled on.

d) Select "Load unpacked" and select the `extension` subdirectory.

d) Pin the extension in Chrome.

Browse the web. If you encounter a website that has the Meta Pixel installed with automatic form data collection, a pop-up will appear that lists what type of data the Meta Pixel is configured to collect.

![An example of how the Chrome Extension appears on a website](extension-example-screenshot.png "Screenshot of Chrome Extension")
