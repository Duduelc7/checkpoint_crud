
$(document).ready(
    function exportPrint() {
        $(document).on("click", "#exportPDF", function () {
            var today = new Date();
            var dd = String(today.getDate()).padStart(2, '0');
            var mm = String(today.getMonth() + 1).padStart(2, '0');
            var yyyy = today.getFullYear();
            var min = today.getMinutes();
            var hour = today.getHours();

            today = 'Relatório emitido em:  ' + dd + '/' + mm + '/' + yyyy + ' às: ' + hour + ':' + min;
            // Create an "li" node:
            const node = document.createElement("h5");
            // Create a text node:
            const textnode = document.createTextNode(today);
            // Append the text node to the "li" node:
            node.appendChild(textnode);

            // Append the "li" node to the list:
            document.getElementById("print-info").appendChild(node);
            window.print();
            document.getElementById("print-info").removeChild(node);
        });
    }
);


function filtrarPorId() {
    var input, filter, table, tr, td, i;
    input = document.getElementById("idFilter");
    filter = input.value.toUpperCase();
    table = document.getElementById("sg-table");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {
            if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}

function filtrarPorEmpresa() {
    var input, filter, table, tr, td, i;
    input = document.getElementById("empresaFilter");
    filter = input.value.toUpperCase();
    table = document.getElementById("sg-table");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[1];
        if (td) {
            if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}

function filtrarPorProjeto() {
    var input, filter, table, tr, td, i;
    input = document.getElementById("projetoFilter");
    filter = input.value.toUpperCase();
    table = document.getElementById("sg-table");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[2];
        if (td) {
            if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}

function filtrarPorCNPJ() {
    var input, filter, table, tr, td, i;
    input = document.getElementById("cnpjFilter");
    filter = input.value.toUpperCase();
    table = document.getElementById("sg-table");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[5];
        if (td) {
            if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}