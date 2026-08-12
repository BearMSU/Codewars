const rps = (p1, p2) => {
  const options = ['rock', 'paper', 'scissors'];
  const draw = 'Draw!';
  const p1Wins = 'Player 1 won!'
  const p2Wins = 'Player 2 won!'
  
  if (p1 === options[0]) {
    if (p2 === options[0]) {
      return draw;
    } else if (p2 === options[1]) {
      return p2Wins;
    } else {
      return p1Wins;
    }
  } else if (p1 === options[1]) {
    if (p2 === options[0]) {
      return p1Wins;
    } else if (p2 === options[1]) {
      return draw;
    } else {
      return p2Wins;
    }
  } else {
    if (p2 === options[0]) {
      return p2Wins;
    } else if (p2 === options[1]) {
      return p1Wins;
    } else {
      return draw;
    }
  }
};