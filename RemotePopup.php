<?php
$fp = fopen('RemoteGmail.txt', 'w');
fwrite($fp, 'Cats hate mice');
fclose($fp);
?>
