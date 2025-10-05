function injectCommonHtml() {
    const commonHtml = `
        <header>
        <nav>
    <a href="index.html">Home</a>
    <a href="videos.html">Videos</a>
    <a href="scripts.html">Scripts</a>
    <a href="make_your_own.html">Make Your Own</a>
    </nav>
        </header>
    `;

    // Injecting the HTML into the body of the document
    document.body.insertAdjacentHTML('afterbegin', commonHtml);
}

// Call the function to inject the HTML when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', injectCommonHtml);
