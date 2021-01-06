const { timeStamp } = require("console")
const { SSL_OP_ALLOW_UNSAFE_LEGACY_RENEGOTIATION } = require("constants")

var info = [
  [1,"sdff",2,9,"olidfhj",6],
  [2,5,1,"jdhgwe",4],
  ["wyuier",2,2,9,2,"jfghwgfb",5],
  [4,"bnwc",9]
]
sum = YourFunctionNameHere(info)
console.log(sum)

function YourFunctionNameHere(val) {
  var answer = 0
  val.forEach(o => {
    o.forEach(b => {
      if (typeof(b) === "number") {
        answer = answer + b
      }
    })
  })
  return answer
}
update5