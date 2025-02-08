function toEditCell(dom) {
    const tableCell = dom.closest('td');
    for (const elem of tableCell.getElementsByClassName('static')) {
        elem.style.display = 'none';
    }
    for (const elem of tableCell.getElementsByClassName('edit')) {
        elem.style.display = 'inline-block';
    }
    tableCell.querySelector('input').focus();
}

function toStaticCell(dom) {
    const tableCell = dom.closest('td');
    for (const elem of tableCell.getElementsByClassName('static')) {
        elem.style.display = 'inline-block';
    }
    for (const elem of tableCell.getElementsByClassName('edit')) {
        elem.style.display = 'none';
    }
}