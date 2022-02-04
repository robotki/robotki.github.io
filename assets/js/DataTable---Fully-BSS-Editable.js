$(document).ready(function() {
    $('.mydatatable').DataTable({
        dom: 'Bfrtip',
        buttons: [
            'copy', 'csv', 'excel', 'pdf', 'print'
        ],
        scrollY: 300,
        scrollX: true,
        autoWidth: false,
        scrollCollapse: true,
        paging: false
    });
});