/**
 * Created by erlan on 5/11/17.
 */
$(document).ready(function () {
    var fileInput = $('#id_images');
    var helpText = $('#file-counter');
    $(fileInput).on('change', function (event) {
        var fileReader = new FileReader();
        fileReader.readAsDataURL(this.files[0]);
        var count = this.files.length;
        var result = '';
        if(count == 1 || count % 10 == 1) {
            result = '<b>Выбран ' + count + ' файл</b>';
        } else if ((count >= 2 && count <= 4) || (count % 10 >= 2 && count % 10 <= 4)) {
            result = '<b>Выбрано ' + count + ' файла</b>';
        } else if (count >= 5) {
            result = '<b>Выбрано ' + count + ' файлов</b>';
        }
        helpText.html(result);
    })
});