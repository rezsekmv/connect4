
export const getMoveFromApi = async (url, board, next_player) => {
    return await fetch(url, {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        next_player: next_player,
        board: board
      })
    })
      .then((response) => response.json())
      .catch((error) => {
        console.error('Can not reach backend');
      });
    };

export const checkWinFromApi = async (url, board) => {
    return await fetch(url, {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        board: board
      })  
    })
      .then((response) => response.json())
      .catch((error) => {
        console.error('Can not reach backend');
      });
    };
