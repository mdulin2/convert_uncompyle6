<?php
$fp = fopen('getonmylevel.txt', 'w');
fwrite($fp, 'Cats hate mice');
fclose($fp);
?>
