<?php

require_once 'config.php';

function fall_down(){
    header("location: index.php?q=ko");
    die("No No No we don't do that here!");
    exit;
}

function dedupe_letters($str){
    $token = $str[0];
    $dedupe = $token;
    for($i = 1; $i < strlen($str); $i++){
        if($token == $str[$i]) continue;
        $token = $str[$i];
        $dedupe .= $token;
    }
    
    return $dedupe;
}

function dedupe_words($str){
    $sq = explode(' ', $str);
    $dedupe = [$sq[0]];
    for($i = 1; $i < count($sq) ; $i++){
        if(! in_array($sq[$i], $dedupe)) $dedupe[] = $sq[$i]; 
    }
    
    return implode(' ', $dedupe);
}

$dirty_words = ['zeb', 'zab', 'lker', 'lkar', 'fuck', 'bitch', 'sex', 'tabon', 'zb', 'porn', 'pornhub', 'xnxx', 'brazzerz', 'xxx', 'xlxx', 'xvideo',
                'xvideos', 'bobs', 'nipples', 'bzazl', 'bzazel', 'tboun', 'tbon', 'tabon', 'taboun', '9lawi', '9lwi', 'qlawi', 'klawi', '9lwa'];

if(isset($_POST['do_insert'])){
    
    $name = addslashes($_POST['name']);
    $question = addslashes($_POST['question']);
    $answer = explode("http", addslashes($_POST['answer']));
    
    // dedupe strings
    $question = dedupe_words(dedupe_letters($question));
    $answer[0] = dedupe_words(dedupe_letters($answer[0]));
    
    
    // clearn question & answer and fall down if dirty
    $tokens = explode(' ', $question);
    foreach($tokens as $t){
        if(in_array($t, $dirty_words)){
            fall_down();
            exit;
        }
    }
    
    // replace ch letters
    $question = str_replace('sh', 'ch', $question);
    $question = str_replace('x', 'ch', $question);
    
    $answer[0] = str_replace('sh', 'ch', $answer[0]);
    $answer[0] = str_replace('x', 'ch', $answer[0]);
    
    $answer = implode("http", $answer);

    // Save username for future usage
    $_SESSION['name'] = $name;
    
    $stmt = $conn->prepare("INSERT INTO hafid (name, question, answer) VALUES (?, ?, ?)");
    $stmt->bind_param("sss", $name, $question, $answer);
    if($stmt->execute()) $resp = "ok";
    else $resp = "ko";
    
    header("location: index.php?q=$resp");
    die("No No No we don't do that here!");
    exit;
    
}

exit;