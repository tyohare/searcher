document.addEventListener('DOMContentLoaded', function() {
  var searchInput = document.getElementById('searchInput');

  searchInput.addEventListener('input', function() {
    search();
  });

  function search() {
    var searchInputValue = searchInput.value.toLowerCase();
    var searchResults = document.getElementById('searchResults');
    searchResults.innerHTML = '';

    fetch('indexed2.json')
      .then(function(response) {
        return response.json();
      })
      .then(function(data) {
        var searchIndex = data.searchindex || [];

        // Filter the search index for objects with a close word match
        var matchedObjects = searchIndex.filter(function(note) {
          return (
            note.title.toLowerCase().includes(searchInputValue) ||
            note.body.toLowerCase().includes(searchInputValue)
          );
        });

        // Display the matched JSON objects
        matchedObjects.forEach(function(note) {
          var resultContainer = document.createElement('div');
          resultContainer.classList.add('result-item');

          var resultTitle = document.createElement('div');
          resultTitle.classList.add('result-title');
          resultTitle.innerHTML = getHighlightedText(note.title, searchInputValue);

          var resultDescription = document.createElement('div');
          resultDescription.classList.add('result-description');
          resultDescription.innerHTML = getHighlightedText(truncateDescription(note.body), searchInputValue);

          resultContainer.appendChild(resultTitle);
          resultContainer.appendChild(resultDescription);

          resultContainer.addEventListener('click', function() {
            window.location.href = note.url;
          });

          searchResults.appendChild(resultContainer);
        });

        if (matchedObjects.length === 0) {
          var noResultsMsg = document.createElement('div');
          noResultsMsg.classList.add('result-item');
          noResultsMsg.textContent = 'No matching results found.';
          searchResults.appendChild(noResultsMsg);
        }
      })
      .catch(function(error) {
        console.log('Error loading search index:', error);
      });
  }

  function getHighlightedText(text, highlight) {
    var regex = new RegExp('(' + highlight + ')', 'gi');
    return text.replace(regex, '<span class="result-highlight">$1</span>');
  }

  function truncateDescription(description) {
    var maxLength = 200;
    if (description.length > maxLength) {
      return description.substring(0, maxLength) + '...';
    }
    return description;
  }
});


