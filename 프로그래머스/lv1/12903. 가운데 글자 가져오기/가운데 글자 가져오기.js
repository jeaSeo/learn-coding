function solution(s) {
    let arry = s.split('');
	let answer;
	let j = arry.length;
	if ( j % 2 == 1 ) {
		let i = Math.round(j / 2);
		answer = arry[i-1];
	} else if ( j % 2 == 0 ) {
		let i = Math.floor(j / 2);
		answer = arry[i-1] + arry[i];
	}
	return answer;
}