function injectCommonHtml() {
    const commonHtml = `
        <header>
        <nav>
    <a href="index.html">Home</a>
    <a href="gaia_test_3.py">gaia_test_3.py</a>
    </nav>
        </header>
    `;

    // Injecting the HTML into the body of the document
    document.body.insertAdjacentHTML('afterbegin', commonHtml);
}

// Call the function to inject the HTML when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', injectCommonHtml);
