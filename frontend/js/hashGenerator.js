async function generateHash() {
    const input = document.getElementById("inputText").value;
    const algorithm = document.getElementById("algorithm").value;
    const resultBox = document.getElementById("resultBox");
    const hashOutput = document.getElementById("hashOutput");
    const algoUsed = document.getElementById("algoUsed");

    if (!input) {
        alert("Please enter some text.");
        return;
    }

    let hash = "";

    if (algorithm === "MD5") {
        hash = md5(input);
    } else if (algorithm === "SHA-1") {
        hash = await shaHash(input, "SHA-1");
    } else if (algorithm === "SHA-256") {
        hash = await shaHash(input, "SHA-256");
    }

    algoUsed.innerText = `Algorithm: ${algorithm}`;
    hashOutput.innerText = hash;
    resultBox.style.display = "block";
}

/* ---------- SHA HASHING USING WEB CRYPTO ---------- */
async function shaHash(message, algo) {
    const encoder = new TextEncoder();
    const data = encoder.encode(message);
    const hashBuffer = await crypto.subtle.digest(algo, data);
    return bufferToHex(hashBuffer);
}

function bufferToHex(buffer) {
    return Array.from(new Uint8Array(buffer))
        .map(b => b.toString(16).padStart(2, "0"))
        .join("");
}
/* ---------- MD5 IMPLEMENTATION ---------- */
/* Lightweight educational implementation */

function md5(string) {
    return CryptoJS.MD5(string).toString();
}
