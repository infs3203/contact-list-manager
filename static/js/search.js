// static/js/search.js (JavaScript)
function performSearch() {
    const searchText = document.getElementById('searchInput').value;
    const groupSelect = document.querySelector('select[name="group"]');
    const groupValue = groupSelect ? groupSelect.value : "";
    const url = `/api/contacts?search=${encodeURIComponent(searchText)}&group=${encodeURIComponent(groupValue)}`;

    fetch(url)
        .then(response => response.json())
        .then(data => {
            const tbody = document.querySelector('tbody');
            tbody.innerHTML = '';
            data.forEach(contact => {
                tbody.insertAdjacentHTML('beforeend', `
                    <tr>
                        <td>${contact.name}</td>
                        <td>${contact.phone}</td>
                        <td>${contact.email}</td>
                        <td>${contact.type}</td>
                        <td>
                            <a href="/update/${contact.id}" class="btn btn-sm btn-primary">Edit</a>
                            <a href="/delete/${contact.id}" class="btn btn-sm btn-danger"
                               onclick="return confirm('Are you sure you want to delete this contact?')">Delete</a>
                        </td>
                    </tr>
                `);
            });
        });
}

document.getElementById('searchInput').addEventListener('input', performSearch);

const groupSelect = document.querySelector('select[name="group"]');
if (groupSelect) {
    groupSelect.addEventListener('change', performSearch);
}