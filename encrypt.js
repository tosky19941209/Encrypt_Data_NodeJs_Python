const { timeStamp } = require('console');
const crypto = require('crypto');
const CryptoJS = require('crypto-js');
const SECRET_KEY = 'mysecretkey1234';


function encrypt(data) {
    const ciphertext = CryptoJS.AES.encrypt(JSON.stringify(data), SECRET_KEY).toString();
    return ciphertext;
}

// Decrypt data
function decrypt(ciphertext) {
    const bytes = CryptoJS.AES.decrypt(ciphertext, SECRET_KEY);
    const originalData = JSON.parse(bytes.toString(CryptoJS.enc.Utf8));
    return originalData;
}

const data = {
    message: " hello",
    timeStamp: 100
}

encryptedData = encrypt(data)
decryptedData = decrypt(encryptedData)
console.log(encryptedData)
console.log(decryptedData)