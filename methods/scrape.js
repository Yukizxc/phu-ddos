const axios = require('axios');
const fs = require('fs');

const proxies = [];
const output_file = 'proxyscrape.txt';

if (fs.existsSync(output_file)) {
  fs.unlinkSync(output_file);
  console.log(`'${output_file}' has been deleted.`);
}

const raw_proxy_sites = [
    'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all',
    'https://www.proxy-list.download/api/v1/get?type=http',
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
    'https://proxyspace.pro/http.txt',
    'https://multiproxy.org/txt_all/proxy.txt',
    'https://api.voidevs.com/v1/proxy-list?protocol=http',
    'https://api.voidevs.com/v1/proxy-list?protocol=all',
    'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all&ssl=yes',
    'https://www.proxy-list.download/api/v1/get?type=http&anon=elite',
    'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt',
];

async function fetchProxies() {
  for (const site of raw_proxy_sites) {
    try {
      const response = await axios.get(site);
      const lines = response.data.split('\n');
      for (const line of lines) {
        if (line.includes(':')) {
          const [ip, port] = line.split(':', 2);
          proxies.push(`${ip}:${port}`);
        }
      }
    } catch (error) {
      console.error(`Failed to get proxy from here ${site}: ${error.message}`);
    }
  }

  fs.writeFileSync(output_file, proxies.join('\n'));
  console.log(`Proxies were successfully downloaded and stored inside ${output_file}`);
}

fetchProxies();