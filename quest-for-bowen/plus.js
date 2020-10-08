const fs = require('fs');
const { dirname } = require('path');
const path = require('path');

/**
 * 结果 500 以内
 */

let split = '--------------';
let day = 1;
let max = 60;
let res = [];
let random = () => {
  return Math.floor(Math.random() * 150) + '';
}
let randomFlag = () => {
  if (Math.random() < 0.5) return '-';
  return '+';
}
let quest = () => {
  return random() + randomFlag() + random() + randomFlag() + random() + '=' + '\n'
}
console.log( quest() );
let content = '';
while (day <= 60) { // 60天
  content += '\n';
  content = content + split + '第' + day + '天' + split + '\n';
  for (let i = 0; i < 10; i++) {
    content += quest();
  }
  day++;
}
fs.writeFileSync(path.resolve(__dirname, 'plus.txt'), content);