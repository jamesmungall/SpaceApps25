function injectCommonHtml() {
    const commonHtml = `
        <header>
        <nav>
    <a href="index.html">Home</a>
    <a href="plotly_chart2.html">Plotly Chart 2</a>
    <a href="ellipse.html">Ellipse</a>
    <a href="stars_0_23pc.csv">CSV for stars within 23pc</a>
    <a href="read_json.html">Read JSON</a>
	</nav>
        </header>
    `;

    // Injecting the HTML into the body of the document
    document.body.insertAdjacentHTML('afterbegin', commonHtml);
}

// Call the function to inject the HTML when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', injectCommonHtml);
