function updateDayRange() {
    var selectedYear = parseInt(document.getElementById("nam_sinh").value);
    var selectedMonth = parseInt(document.getElementById("thang_sinh").value);
    if (selectedYear == "" || selectedMonth == "") {
        return;
    }
    var dayRange = selectedMonth == 2 ? (selectedYear % 4 == 0 && selectedYear % 100 != 0 || selectedYear % 400 == 0 ? 29 : 28) : ([1, 3, 5, 7, 8, 10, 12].includes(selectedMonth) ? 31 : 30);
    var dayOptions = document.createElement("option");
    let daySelectBox = document.getElementById("ngay_sinh");
    while (daySelectBox.options.length > 0) {
        daySelectBox.remove(0);
    }
    for (let i = 1; i <= dayRange; i++) {
        let val = (i < 10 ? "0" + i : i).toString();
        let newOption = new Option(val, val);
        const daySelect = document.querySelector("#ngay_sinh");
        daySelect.add(newOption, undefined);
        // }
    }
}