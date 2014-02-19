function quickSort(array, less) {
 
  function swap(i, j) { var t=array[i]; array[i]=array[j]; array[j]=t }
 
  function sort(left, right) {
 
    if (left < right) {
 
      var pivot = array[(left + right) >> 1];
      var left_new = left, right_new = right;
 
      do {
        while (less(array[left_new], pivot))
          left_new++;
        while (less(pivot, array[right_new]))
          right_new--;
        if (left_new  <= right_new)
          swap(left_new++, right_new--);
      } while (left_new  <= right_new);
 
      sort(left, right_new);
      sort(left_new, right);
 
    }
  }
 
  sort(0, array.length-1);
 
  return array;
}

function bubbleSort(array,less) {
	var i=0;
	var j=0;
	function swap(i, j) { var t=array[i]; array[i]=array[j]; array[j]=t }
	for (i=array.length;i>2;i--) {
		for (j=1;j<i-1;j++) {
			if (less(array[j+1],array[j])) {
				swap(j,j+1)
			}
		}
	}
	return array
}