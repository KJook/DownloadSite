function b64Encode (str) {
    return btoa(encodeURIComponent(str));
}
function b64Decode (str) {
    return decodeURIComponent(atob(str));
}