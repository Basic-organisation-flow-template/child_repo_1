// src/index.test.js
import { greet, add } from './index';

describe('greet function', () => {
  test('should return a greeting with the given name', () => {
    expect(greet('World')).toBe('Hello, World!');
  });
});

describe('add function', () => {
  test('should return the sum of two numbers', () => {
    expect(add(2, 3)).toBe(5);
  });
});