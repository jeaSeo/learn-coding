function solution(n) {
	let insert = n.toString().split('');
	var answer = 0;
	for ( var i = 0; i < insert.length; i++ ) {
		insert[i] = Number(insert[i]);
		answer += insert[i];
	}
    return answer;
}