
document.getElementById('toggleSidebar').addEventListener('click', function () {
    var sidebar = document.getElementById('sidebar-container');
    var mainContent = document.getElementById('main-content');

    if (sidebar.style.display === 'none') {
        sidebar.style.display = 'block';
        mainContent.classList.remove('centralized-content');
        this.textContent = 'Ocultar Sidebar';
    } else {
        sidebar.style.display = 'none';
        mainContent.classList.add('centralized-content');
        this.textContent = 'Mostrar Sidebar';
    }
});
