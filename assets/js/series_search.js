let debounceTimer;

const debounceSearch = (e) => {
	if (debounceTimer) {
		clearTimeout(debounceTimer);
	}
	debounceTimer = setTimeout(search, 500, e.target.value);
};

const search = (searchVal) => {
	const noResults = document.getElementById('no-results');
	
	const filtered_books = books.filter((book) => (
		!searchVal
		|| (book.isbn10 && book.isbn10.includes(searchVal))
		|| (book.isbn13 && book.isbn13.includes(searchVal))
		|| book.title.toLowerCase().includes(searchVal.toLowerCase())
		|| book.author_names.some((author) => author.toLowerCase().includes(searchVal.toLowerCase()))
		|| book.editor_names.some((editor) => editor.toLowerCase().includes(searchVal.toLowerCase()))
		|| (book.year && book.year.includes(searchVal))
		|| (book.volume && book.volume.includes(searchVal))
	));
	
	document.querySelector('.book-list').querySelectorAll('li').forEach((book) => {
		if (filtered_books.some((b) => b.url === book.dataset.url)) {
			// Book matches the filter, show the link
			book.style.display = '';
		} else {
			// Book doesn't match the filter, hide the link
			book.style.display = 'none';
		}
	});
	
	if (noResults) {
		if (filtered_books.length === 0) {
			// Show message indicating there are no results
			noResults.style.display = '';
		} else {
			// Hide no results message since there are results
			noResults.style.display = 'none';
		}
	}
};
window.addEventListener('pageshow', () => {
	search(document.querySelector("input[type='search']").value);
});