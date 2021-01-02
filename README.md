
#<span style="color:darkred"> TİCARET ÜNİVERSİTESİ</span>


### <span style="color:darkblue"> Histogram </span>

Verilerin sütun grafiğiyle gösterilmesine histogram adı verilir.

###PDF

Olasılık dağılım fonksiyonu.

###CDF

Kümülatif dağılım fonksiyonu.

###Tahmini Ortalama Değer

###Gerçek Ortalama Değer

###Ortalama Değer Sapması

Gerçek ve tahmini ortalama değer farkı.

###Tahmini Varyans

###Gerçek Varyans

###Varyans Değer Sapması

Gerçek ve tahmini varyans değer farkı.

###Faktöriyel

Kullanıcıdan alınan değerin faktöriyelinin hesaplanması.

###Moment Vektörü

###Moment Vektörü Türevi

Oluşturulan moment vektörünün istenilen mertebeden türevinin alınması.

## <span style="color:darkblue"> GİRDİLER </span>

-Veri Uzunluğu / NO_OF_BINS

-Örnekler Sayısı / NO_OF_SAMPLES

-Moment Sayısı / NO_OF_MOMENTS

-Başlangıç Noktası / START_POINT

-Bitiş Noktası / STOP_POINT



## <span style="color:darkblue">GEREKLİLİKLER </span>

-Python 3.9

-numpy kütüphanesi 

## <span style="color:darkblue"> ÖRNEK </span>
####--------------------- REPORT ---------------------
--------------------------------------------------
NO_OF_BINS = 100

NO_OF_SAMPLES = 10000

NO_OF_MOMENTS = 30

START_POINT = -1

STOP_POINT = 3

--------------------------------------------------

Estimated mean = 0.9888242424242426

True mean = 1.0088260523176833

Error in mean estimation =  0.020001809893440692

--------------------------------------------------

Estimated variance  2.3049945107642085

True variance = 2.3454313420979576

Error in variance = 0.020001809893440692

--------------------------------------------------

Number of operations to obtain mean with PDF =  100

Number of operations to obtain mean without PDF =  10000

Performance improvement =  0.99

--------------------------------------------------

Estimated x3 = 4.886062310277555

true_x3 = 5.026480441424946

Estimated x3 error =  0.1404181311473911

--------------------------------------------------

Factorial Output =  120

--------------------------------------------------

moment_array = [1.00000000e+00 9.88824242e-01 2.30499451e+00 4.88606231e+00
 1.18498084e+01 2.92013993e+01 7.46278680e+01 1.94107061e+02
 5.13340277e+02 1.37396993e+03 3.71476275e+03 1.01261303e+04
 2.77949055e+04 7.67438650e+04 2.12975558e+05 5.93661900e+05
 1.66127158e+06 4.66489966e+06 1.31396470e+07 3.71132531e+07
 1.05090244e+08 2.98252520e+08 8.48218531e+08 2.41689552e+09
 6.89871581e+09 1.97233376e+10 5.64732038e+10 1.61922799e+11
 4.64874425e+11 1.33625105e+12]

Moment array first derivative =  [-1.11757576e-02  1.31617027e+00  2.58106780e+00  6.96374608e+00
  1.73515909e+01  4.54264687e+01  1.19479193e+02  3.19233216e+02
  8.60629649e+02  2.34079283e+03  6.41136752e+03  1.76687752e+04
  4.89489595e+04  1.36231693e+05  3.80686341e+05  1.06760968e+06
  3.00362808e+06  8.47474738e+06  2.39736060e+07  6.79769911e+07
  1.93162276e+08  5.49966010e+08  1.56867699e+09  4.48182030e+09
  1.28246218e+10  3.67498661e+10  1.05449596e+11  3.02951626e+11
  8.71376620e+11  0.00000000e+00]

--------------------------------------------------

moment array  2 value = 2.3049945107642085

n_th_order_difference(moment_array, n) 2 value = 2.3049945107642085

Number of Derivative = 0

Our Derivative = [1.00000000e+00 9.88824242e-01 2.30499451e+00 4.88606231e+00
 1.18498084e+01 2.92013993e+01 7.46278680e+01 1.94107061e+02
 5.13340277e+02 1.37396993e+03 3.71476275e+03 1.01261303e+04
 2.77949055e+04 7.67438650e+04 2.12975558e+05 5.93661900e+05
 1.66127158e+06 4.66489966e+06 1.31396470e+07 3.71132531e+07
 1.05090244e+08 2.98252520e+08 8.48218531e+08 2.41689552e+09
 6.89871581e+09 1.97233376e+10 5.64732038e+10 1.61922799e+11
 4.64874425e+11 1.33625105e+12]

Numpy test Derivative = [1.00000000e+00 9.88824242e-01 2.30499451e+00 4.88606231e+00
 1.18498084e+01 2.92013993e+01 7.46278680e+01 1.94107061e+02
 5.13340277e+02 1.37396993e+03 3.71476275e+03 1.01261303e+04
 2.77949055e+04 7.67438650e+04 2.12975558e+05 5.93661900e+05
 1.66127158e+06 4.66489966e+06 1.31396470e+07 3.71132531e+07
 1.05090244e+08 2.98252520e+08 8.48218531e+08 2.41689552e+09
 6.89871581e+09 1.97233376e+10 5.64732038e+10 1.61922799e+11
 4.64874425e+11 1.33625105e+12]

Difference between 2 derivative  =  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0.]


**************************************************

moment array  2 value = 2.3049945107642085

n_th_order_difference(moment_array, n) 2 value = 2.581067799513346

Number of Derivative = 1

Our Derivative = [-0.011175757575757839, 1.3161702683399659, 2.581067799513346, 
6.963746080627595, 17.35159094882581, 45.42646866514566, 119.47919340671145, 
319.23321599335515, 860.6296486553551, 2340.7928260333993, 6411.367521840558, 
17668.775180805562, 48948.95952913818, 136231.69346807175, 380686.341306761,
 1067609.6810964802, 3003628.0835050056, 8474747.375626191, 23973606.020352624,
 67976991.1128304, 193162276.17181495, 549966010.4142776, 1568676988.1853564,
 4481820295.87163, 12824621812.887663, 36749866136.77604, 105449595500.6506, 
 302951626233.3652, 871376619560.526]

Numpy test Derivative = [-1.11757576e-02  1.31617027e+00  2.58106780e+00  6.96374608e+00
  1.73515909e+01  4.54264687e+01  1.19479193e+02  3.19233216e+02
  8.60629649e+02  2.34079283e+03  6.41136752e+03  1.76687752e+04
  4.89489595e+04  1.36231693e+05  3.80686341e+05  1.06760968e+06
  3.00362808e+06  8.47474738e+06  2.39736060e+07  6.79769911e+07
  1.93162276e+08  5.49966010e+08  1.56867699e+09  4.48182030e+09
  1.28246218e+10  3.67498661e+10  1.05449596e+11  3.02951626e+11
  8.71376620e+11]

Difference between 2 derivative  =  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0.]
 1.
 
**************************************************

moment array  2 value = 2.3049945107642085

n_th_order_difference(moment_array, n) 2 value = 4.382678281114249

Number of Derivative = 2

Our Derivative = [1.3273460259157237, 1.2648975311733803, 4.382678281114249,
 10.387844868198215, 28.074877716319854, 74.05272474156578, 199.7540225866437,
 541.396432662, 1480.163177378044, 4070.5746958071586, 11257.407658965003, 
 31280.184348332616, 87282.73393893358, 244454.64783868927, 686923.3397897192,
 1936018.4024085253, 5471119.292121186, 15498858.644726433, 44003385.092477776,
 125185285.05898455, 356803734.24246264, 1018710977.7710788, 2913143307.6862736, 
 8342801517.016033, 23925244323.888374, 68699729363.874565, 197502030732.71457, 568424993327.1609]

Numpy test Derivative = [1.32734603e+00 1.26489753e+00 4.38267828e+00 1.03878449e+01
 2.80748777e+01 7.40527247e+01 1.99754023e+02 5.41396433e+02
 1.48016318e+03 4.07057470e+03 1.12574077e+04 3.12801843e+04
 8.72827339e+04 2.44454648e+05 6.86923340e+05 1.93601840e+06
 5.47111929e+06 1.54988586e+07 4.40033851e+07 1.25185285e+08
 3.56803734e+08 1.01871098e+09 2.91314331e+09 8.34280152e+09
 2.39252443e+10 6.86997294e+10 1.97502031e+11 5.68424993e+11]

Difference between 2 derivative  =  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0.]


**************************************************

#License and Citation

The software is licensed under the MIT License.


