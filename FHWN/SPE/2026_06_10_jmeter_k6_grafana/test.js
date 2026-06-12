import http from 'k6/http';
import { check, sleep } from 'k6';
import { SharedArray } from 'k6/data'


const ranges = new SharedArray('ranges', function () {
  return [
    { start: 10000, end: 11000 },
    { start: 11000, end: 12000 },
    { start: 12000, end: 13000 },
    { start: 13000, end: 14000 },
    { start: 14000, end: 15000 },
    { start: 15000, end: 16000 },
    { start: 16000, end: 17000 },
    { start: 17000, end: 18000 },
    { start: 18000, end: 19000 },
    { start: 19000, end: 20000 },
  ];
});


export const options = {
  scenarios: {
    load_test: {
      executor: 'constant-vus',
      vus: 20,
      duration: '45s',
      startTime: '0s',
    },
    stress_test: {
      executor: 'ramping-vus',
      startVUs: 0,
      stages: [
        { duration: '1m', target: 150 },
        { duration: '2m', target: 150 }, 
        { duration: '30s', target: 0 },  
      ],
      startTime: '2m', 
    },
    spike_test: {
      executor: 'ramping-vus',
      startVUs: 0,
      stages: [
        { duration: '30s', target: 400 }, 
        { duration: '30s', target: 10 }, 
        { duration: '2m', target: 10 },  
      ],
      startTime: '6m', 
    },
  },
  thresholds: {
    http_req_duration: ['p(95)<3000'], 
  },
};

// 2. The code that each Virtual User actually runs
export default function () {
  const range = ranges[Math.floor(Math.random() * ranges.length)];
  let res = http.get(`http://127.0.0.1:5000/primes/${range.start}/${range.end}`);
  
  
  check(res, {
    'is status 200': (r) => r.status === 200,
    'is json': (r) => {
      try {
        JSON.parse(r.body);
        return true;
      } catch {
        return false;
      }
    },
    'is array': (r) => {
      try {
        return Array.isArray(JSON.parse(r.body));
      } catch {
        return false;
      }
    },
    'array size between 5 and 500': (r) => {
      try {
        const data = JSON.parse(r.body);
        return Array.isArray(data) && data.length > 5 && data.length < 500;
      } catch {
        return false;
      }
    },
  });

  sleep(1); 
}