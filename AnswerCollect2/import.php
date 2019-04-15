<?php
    error_reporting(E_ALL & ~E_NOTICE);
    $db_host = "10.147.17.170";
    $db_user = "root";
    $db_pass = "root";
    $db_name = "erya";
    $conn = new mysqli($db_host, $db_user, $db_pass, $db_name);
    if ($conn->connect_error) {
        $ret['msg'] = $conn->connect_error;
        return json_encode($ret);
    }
    $file = fopen("list.csv", "r") or die("Unable to open file!");
    $list = [];
    while( !feof($file) ) {
        $line = fgets($file);
        $line = explode(",", $line, 2);
        array_push($list, ['question' => $line[0], 'answer' => $line[1] ]);
    }
    fclose($file);
    $i = 1;
    foreach ($list as $key => $value) {
        $sql = "SELECT * FROM `question` WHERE `question` = '" . $value['question'] . "'";
        $result = $conn->query($sql);
        if ($result->num_rows) {
            $sql2 = "UPDATE `question` SET `answer` = '" . $value['answer'] . "' WHERE `question` = '" . $value['question'] . "'";
            $conn->query($sql2);
            print_r($i . '.' .$value['question'] . '------更新成功\r\n');
        } else {
            $sql2 = "INSERT INTO `question` VALUES (null, '" . $value['question'] . "', '" . $value['answer'] . "')";
            $conn->query($sql2);
            print_r($i . '.' .$value['question'] . '------插入成功\r\n');
        }
        $i++;
    }
?>