function injectCommonHtml() {
    const commonHtml = `
        <header>
        <nav>
    <a href="index.html">Home</a>
    <a href="videos.html">Videos</a>
    <a href="scripts.html">Scripts</a>
    <a href="gaia_test_3.txt">gaia_test_3.txt</a>
    </nav>
        </header>
    `;

    // Injecting the HTML into the body of the document
    document.body.insertAdjacentHTML('afterbegin', commonHtml);
}

// Call the function to inject the HTML when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', injectCommonHtml);
