<?php

// $origCokie = base64_decode('ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D');

// function xor_encrypt($in)
// {
//     $key = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));
//     $text = $in;
//     $outText = '';

//     // Iterate through each character
//     for ($i=0;$i<strlen($text);$i++) {
//         $outText .= $text[$i] ^ $key[$i % strlen($key)];
//     }

//     return $outText;
// }

// print xor_encrypt($origCokie);

function xor_encrypt()
{
    $key = 'qw8J';
    $text = json_encode(array( "showpassword"=>"yes", "bgcolor"=>"#ffffff"));
    $outText = '';

    // Iterate through each character
    for ($i=0;$i<strlen($text);$i++) {
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

print base64_encode(xor_encrypt());
