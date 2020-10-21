import {Dimensions} from 'react-native';

export const windowHeight = Dimensions.get('window').height;
export const windowWidth = Dimensions.get('window').width;
export const ROWNUM = 6;
export const COLNUM = 7;

export const webWidth = 80;
export const webHeigth = 50;

//export const URLmove = 'http://localhost:5000/move';

export const URLmove = 'http://152.66.239.241:5000/move';
export const URLcheckwin = 'http://152.66.239.241:5000/checkwin';

export const playerValues = ['human', 'minmax'];

export function padding(a, b, c, d) {
    return {
      paddingTop: a+'%',
      paddingRight: b ? b+'%' : a+'%',
      paddingBottom: c ? c+'%' : a+'%',
      paddingLeft: d ? d+'%' : (b ? b+'%' : a+'%')
    }
  }