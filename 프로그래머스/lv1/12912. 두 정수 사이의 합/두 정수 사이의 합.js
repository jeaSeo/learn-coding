function solution(a, b) {
	var step = Math.abs(b - a);
	var add  = [a,b];
    var answer = 0;

	for (var i = 0; i < step-1; i++ ) {
		if ( a < b ) {
			add.push(a+1);
            a++;
		} else if ( b < a ) {
			add.push(b+1);
            b++;
		}
	}
	for(var i = 0; i < add.length; i++ ) {
		if ( a == b ) {
			return a;
		} else { 
			answer += add[i];
		}
	}
    return answer;
}