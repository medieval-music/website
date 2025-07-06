let debounceTimer;

const debounceSearch = (e) => {
	if (debounceTimer) {
		clearTimeout(debounceTimer);
	}
	debounceTimer = setTimeout(search, 500, e.target.value);
};

const search = (searchVal) => {
	const sections = document.querySelectorAll('h2');
	const bookLists = document.querySelectorAll('.book-list');
	const quickLinksContainer = document.querySelector('nav.sticky-list-nav');
	const noResults = document.getElementById('no-results');
	
	const filtered_books = books.filter((book) => (
		!searchVal
		|| (book.isbn10 && book.isbn10.includes(searchVal))
		|| (book.isbn13 && book.isbn13.includes(searchVal))
		|| book.title.toLowerCase().includes(searchVal.toLowerCase())
		|| book.author_names.some((author) => author.toLowerCase().includes(searchVal.toLowerCase()))
		|| book.editor_names.some((editor) => editor.toLowerCase().includes(searchVal.toLowerCase()))
		|| (book.year && book.year.includes(searchVal))
	));
	const letters = new Set(filtered_books.map((book) => book.group_letter));
	
	sections.forEach((section) => {
		if (!letters.has(section.textContent)) {
			// No filtered books in the section, hide the header
			section.style.display = 'none';
		} else {
			// Section contains books, show the header
			section.style.display = '';
		}
	});
	
	bookLists.forEach((list) => {
		if (!letters.has(list.dataset.letter)) {
			// None of the books in the list match the filter, hide the entire list
			list.style.display = 'none';
		} else {
			// At least one book in the list matches the filter, need to filter individual books
			list.style.display = '';
			
			list.querySelectorAll('li').forEach((book) => {
				if (filtered_books.some((b) => b.url === book.dataset.url)) {
					// Book matches the filter, show the link
					book.style.display = '';
				} else {
					// Book doesn't match the filter, hide the link
					book.style.display = 'none';
				}
			});
		}
	});
	
	if (noResults) {
		if (letters.size === 0) {
			// Show message indicating there are no results
			noResults.style.display = '';
		} else {
			// Hide no results message since there are results
			noResults.style.display = 'none';
		}
	}
	
	if (quickLinksContainer) {
		if (letters.size < 2) {
			// less that 2 matches, hide all the quick links
			// Quick links only become useful if there's 2 or more matches
			quickLinksContainer.style.display = 'none';
		} else {
			quickLinksContainer.style.display = '';
			quickLinksContainer.querySelectorAll('li').forEach((quickLink) => {
				if (!filtered_books.some((book) => book.group_letter === quickLink.dataset.letter)) {
					// No filtered books in the section, hide the quick link
					quickLink.style.display = 'none';
				} else {
					// Section contains books, show the quick link
					quickLink.style.display = '';
				}
			});
		}
	}
};
window.addEventListener('pageshow', () => {
	search(document.querySelector("input[type='search']").value);
});