export default function (BrowserPolicy) {
  BrowserPolicy.content.allowOriginForAll("*");
  BrowserPolicy.content.allowFontDataUrl();
}
