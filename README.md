# ML2018_410421231
A.the way how you prepare the training samples

B.	all parameters, such as MaxIterLimit, α , and 𝜖 , you used for the training algorithm

C.	the derived weight vector 𝐰

weight =  [0.24914331 0.6613819  0.08923953]

D.	the printed image 𝐼’ decrypted from 𝐸’

decrypted from 𝐸.png

E.	the problems you encountered

一開始我是用cv2來讀檔，結果寫到最後一直有一個bug在weight[0] = weight[0] + a*e*xk[0]這裡
，顯示setting an array element with a sequence.
最後就一個一個print，就發現key跟e的值print來的值不是預期的那樣，是類似array的值
，我就改用imageio來讀檔，就順利進行了。
然後過程中有不知道要使用用甚麼package或是函式就上網查。

F.	what you have learned from this work.
學習到如何使用single-layer neural network 來解碼圖片
