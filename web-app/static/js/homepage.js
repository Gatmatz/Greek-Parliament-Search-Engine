function submitSearch() {
    const query = document.getElementById("search-input").value;
    if (query) {
        window.location.href = "/query_results?query=" + query;
    }
}
document.getElementById("search-input").addEventListener("keyup", function(event) {
    if (event.key === "Enter") {
        submitSearch();
    }
});