function isWebRTCSupported() {
  // --------- Detect if system supports WebRTC 1.0 or WebRTC 1.1.
  return [
    "RTCPeerConnection",
    "webkitRTCPeerConnection",
    "mozRTCPeerConnection",
    "RTCIceGatherer",
  ].reduce(function (acc, item) {
    return acc ? acc : (item in window);
  }, false)
}
