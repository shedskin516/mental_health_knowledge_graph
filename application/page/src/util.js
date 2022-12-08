export function getOptions(arr) {
    let options = arr.map(function(ele){
        return {'text': ele, 'value': ele}
    })
    return options
}