pass_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pypass Web</title>
  <link rel="icon" href="https://raw.githubusercontent.com/h471x/password_generator/master/imgs/pypass.png">
  <style>
    *, *:before, *:after{
      padding: 0;
      margin: 0;
      box-sizing: border-box;
      outline: none;
    }

    body{
      height: 100vh;
      background: #010409;
    }

    .container{
      width: 40%;
      min-width: 450px;
      background-color: #0d1117;
      padding: 80px 30px;
      position: absolute;
      transform: translate(-50%,-50%);
      top: 50%;
      left: 50%;
      border-radius: 8px;
      box-shadow: 0 15px 20px rgba(0,0,0,0.15);
    }

    #output, #exclude{
      background-color: transparent;
      border: none;
      border-bottom: 2px solid #e2e2e2;
      width: 60%;
      height: 35px;
      padding: 20px 5px;
      font-family: Arial;
      color: #f5F5F5;
      font-size: 18px;
      letter-spacing: 1px;
      margin-bottom: 15px;
    }

    button{
      height: 40px;
      width: 50px;
      background-color: transparent;
      color: #fff;
      cursor: pointer;
    }

    button:active{
      height: 40px;
      width: 50px;
      background-color: #ffffff;
      color: #030303;
      cursor: pointer;
    }

    #copy{
      margin-left: 10%;
    }

    input[type="range"]{
      -webkit-appearance: none;
      appearance: none;
      width: 85%;
      height: 3.5px;
      margin-top: 80px;
      background-color: #008bfd;
      border-radius: 3.5px;
    }

    input[type="range"]::-webkit-slider-thumb{
      -webkit-appearance: none;
      appearance: none;
      background: #008bfd;
      border-radius: 50%;
      height: 20px;
      width: 20px;
    }

    h3{
      font-family: arial;
      display: inline-block;
      width: 10%;
      color: #1c1e21;
      background-color: #fff;
      text-align: center;
      padding: 5px 0;
      margin-left: 3%;
      border-radius: 3px;
      font-size: 18px;
    }
  </style>
</head>
<body>
  <div class="container">
    <input type="text" id="output" placeholder="Generated Password">
    <input type="text" id="exclude" placeholder="Exclude Characters">
    
    <button onclick="copyClipboard()" id="copy">Copy</button>
    <button onclick="genPassword()">Gen</button>

    <input type="range" name="" id="length" min="8" max="20" value="8" oninput="genPassword()">
    <h3 id="length-val">8</h3>
  </div>
  <script>
    const defaultCharacters = `abcdefghiljklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890&é"'()-è_çà)=+@^\|[]#~$£%ù!§:/;.?`;
    let output = document.getElementById("output");
    let excludeInput = document.getElementById("exclude");

    function randomValue(value){
      return Math.floor(Math.random() * value);
    };

    function genPassword(){
      let length = document.getElementById("length").value;
      document.getElementById("length-val").textContent = length;
      let str = '';
      let excludeChars = excludeInput.value.split('').map(char => char.trim());
      let characters = defaultCharacters.split('').filter(char => !excludeChars.includes(char)).join('');

      for(let i = 0; i < length; i++){
        let random = randomValue(characters.length);
        str += characters.charAt(random);
      }
      output.value = str;
    };

    function copyClipboard(){
      output.select();
      document.execCommand('copy');
      console.log("Password Copied!");
    };

    genPassword();
  </script>
</body>
</html>
'''

passgen_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pypass Web</title>
  <link rel="icon" href="https://raw.githubusercontent.com/h471x/password_generator/master/imgs/pypass.png">
  <style>
    *, *:before, *:after {
      padding: 0;
      margin: 0;
      box-sizing: border-box;
      outline: none;
    }

    body {
      height: 100vh;
      background: #010409;
    }

    .container {
      width: 40%;
      min-width: 450px;
      background-color: #0d1117;
      padding: 80px 30px;
      position: absolute;
      transform: translate(-50%, -50%);
      top: 50%;
      left: 50%;
      border-radius: 8px;
      box-shadow: 0 15px 20px rgba(0,0,0,0.15);
    }

    #output, #exclude {
      background-color: transparent;
      border: none;
      border-bottom: 2px solid #e2e2e2;
      width: 60%;
      height: 35px;
      padding: 20px 5px;
      font-family: Arial;
      color: #f5F5F5;
      font-size: 18px;
      letter-spacing: 1px;
      margin-bottom: 15px;
    }

    button {
      height: 40px;
      width: 50px;
      background-color: transparent;
      color: #fff;
      cursor: pointer;
    }

    button:active {
      background-color: #ffffff;
      color: #030303;
    }

    #copy {
      margin-left: 10%;
    }

    input[type="range"] {
      -webkit-appearance: none;
      appearance: none;
      width: 85%;
      height: 3.5px;
      margin-top: 80px;
      background-color: #008bfd;
      border-radius: 3.5px;
    }

    input[type="range"]::-webkit-slider-thumb {
      -webkit-appearance: none;
      appearance: none;
      background: #008bfd;
      border-radius: 50%;
      height: 20px;
      width: 20px;
    }

    h3 {
      font-family: Arial;
      display: inline-block;
      width: 10%;
      color: #1c1e21;
      background-color: #fff;
      text-align: center;
      padding: 5px 0;
      margin-left: 3%;
      border-radius: 3px;
      font-size: 18px;
    }
  </style>
</head>
<body>
  <div class="container">
    <input type="text" id="output" placeholder="Generated Password" readonly>
    <input type="text" id="exclude" placeholder="Exclude Characters">
    
    <button type="button" onclick="copyClipboard()" id="copy">Copy</button>
    <button type="button" id="generate">Gen</button>

    <input type="range" name="length" id="length" min="8" max="20" value="8" oninput="updateLength()">
    <h3 id="length-val">8</h3>
  </div>
  <script>
    function updateLength() {
      const length = document.getElementById('length').value;
      document.getElementById('length-val').textContent = length;
      generatePassword(length);
    }

    function generatePassword(length) {
      const exclude = document.getElementById('exclude').value;
      fetch('/generate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({ length: length, exclude: exclude }),
      })
      .then(response => response.json())
      .then(data => {
        document.getElementById('output').value = data.password;
      })
      .catch(error => console.error('Error:', error));
    }

    document.getElementById('generate').onclick = function() {
      const length = document.getElementById('length').value;
      generatePassword(length);
    };

    function copyClipboard() {
      const output = document.getElementById("output");
      output.select();
      document.execCommand('copy');
      console.log("Password Copied!");
    }

    // Initial password generation
    generatePassword(8);
  </script>
</body>
</html>
'''