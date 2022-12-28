[![Downloads](https://static.pepy.tech/personalized-badge/finpy-tse?period=total&units=international_system&left_color=black&right_color=green&left_text=Downloads)](https://pepy.tech/project/finpy-tse)

<div dir="rtl" align="right">

##### این ماژول با هدف دسترسی به اطلاعات مربوط به سهام بورس ایران در محیط برنامه‌نویسی پایتون توسعه یافته است. بنابراین شما می‌توانید به راحتی به داده‌های مدنظر خود دسترسی داشته باشید و در توسعه مدل‌های تحلیلی خود از تحلیل تکنیکال گرفته تا تحلیل‌های عددی و یا مبتنی بر ماشین لرنینگ، استفاده کنید. این ماژول از جامعیت و انعطاف‌پذیری فوق‌العاده‌ای در دسترسی به دیتا و پیش‌پردازش آن برخوردار بوده و می‌تواند جایگزین رایگان و مناسبی برای یک اشتراک پولی، به منظور دسترسی به داده‌های بازار سهام باشد. داده‌های خروجی توابع این ماژول، دیتافریم پانداز بوده و شما می‌توانید از آن به عنوان ورودی سایر ماژول‌های آماده موجود از ماژول‌های مصورسازی گرفته تا ماژول‌های تحلیل تکنیکال، مدیریت پرتفوی و ... استفاده کنید

<p>&nbsp;</p>



#### : ازجمله ویژگی‌های مهم این ماژول می‌توان به موارد زیر اشاره کرد
 
قابلیت دسترسی به داده‌های یک سهم با استفاده از نماد يا نام کامل فارسی  &emsp; <--- &emsp;  <br />
قابلیت انجام تعدیل قیمت به صورت یکجا با احتساب انواع افزایش سرمایه و پرداخت سود نقدی  &emsp; <--- &emsp;  <br />
هوشمندی در تشخیص جابجایی یک نماد بین بازارهای مختلف و یکپارچه سازی همه سوابق نمادهای دارای جابجایی &emsp; <--- &emsp;  <br />
قابلیت دسترسی به سوابق همه شاخص‌های بازار بورس و هوشمندی در تشخیص اشتباهات املایی و نگارشی عناوین شاخص صنایع بورسی  &emsp; <--- &emsp;  <br />
قابلیت دسترسی به سابقه داده‌های درون‌روز یک نماد شامل عمق بازار و ریز معاملات  &emsp; <--- &emsp;  <br />
قابلیت دسترسی و رصد لحظه‌ای دیده‌بان و عمق بازار در ساعت انجام معاملات در بازار  &emsp; <--- &emsp;  <br />
قابلیت تهیه لیست جامعی از مشخصات همه سهم‌های بازار  &emsp; <--- &emsp;  <br />
قابلیت دانلود دسته‌جمعی سابقه قیمت لیستی از سهم‌ها و ساخت پنل قیمت پایانی تعدیل شده برای آنها  &emsp; <--- &emsp;  <br />
قابلیت دسترسی به سابقه ۱۰ ساله قیمت دلار بازار آزاد  &emsp; <--- &emsp;  <br />
خروجی سازگار با دیتافریم پانداز و قابلیت فیلترینگ زمانی مجدد بر اساس تاریخ شمسی  &emsp; <--- &emsp;  <br />
قابلیت ارائه تاریخ شمسی، میلادی و نام ایام هفته برای داده‌های روزانه  &emsp; <--- &emsp;  <br />

<p>&nbsp;</p>

##### این ماژول دارای یک کتابچه راهنمای فارسی است که در آن همه توابع ماژول به همراه مثال ذکر شده است. برای دسترسی به این کتابچه راهنما میتوانید از [این صفحه](https://github.com/ARahimiQuant/finpy-tse) استفاده کنید   

##### همچین می‌توانید از طریق [این لینک](https://t.me/FinPy) به آدرس تلگرامی ما دسترسی داشته باشید

</div>


<p>&nbsp;</p>
<p>&nbsp;</p>

<div dir="rtl" align="right">

# نصب ماژول

</div>

```python
pip install finpy-tse
```


<p>&nbsp;</p>

<div dir="rtl" align="right">

# فراخوانی ماژول


</div>


```python
import finpy_tse as fpy
```

<p>&nbsp;</p>

<div dir="rtl" align="right">

# دریافت سابقه اطلاعات روزانه یک نماد
<hr style="border:2px solid gray"> </hr>




### : دریافت سابقه قیمت

</div>

```python
fpy.Get_Price_History(
    stock='خودرو',
    start_date='1400-01-01',
    end_date='1401-01-01',
    ignore_date=False,
    adjust_price=False,
    show_weekday=False,
    double_date=False)
```


<div dir="rtl" align="right">

### : دریافت سابقه حقیقی-حقوقی

</div>

```python
fpy.Get_RI_History(
    stock='خودرو',
    start_date='1400-01-01',
    end_date='1401-01-01',
    ignore_date=False,
    show_weekday=False,
    double_date=False)
```

<p>&nbsp;</p>

<div dir="rtl" align="right">

# دریافت سابقه اطلاعات درون‌ریز یک نماد
<hr style="border:2px solid gray"> </hr>


### : دریافت سابقه ریز معاملات

</div>

```python
fpy.Get_IntradayTrades_History(
    stock='وخارزم',
    start_date='1400-09-15',
    end_date='1400-12-29',
    jalali_date=True,
    combined_datatime=False,
    show_progress=True)
```

<div dir="rtl" align="right">

### : دریافت سابقه عمق بازار

</div>

```python
fpy.Get_IntradayOB_History(
    stock='کرمان',
    start_date='1400-08-01',
    end_date='1400-08-01',
    jalali_date=True,
    combined_datatime=False,
    show_progress=True)
```

<div dir="rtl" align="right">

### : دریافت سابقه ارزش صف در زمان بسته‌شدن بازار

</div>

```python
fpy.Get_Queue_History(
    stock='وخارزم',
    start_date='1400-09-15',
    end_date='1400-12-29',
    show_per_capita=True,
    show_weekday=False,
    double_date=False,
    show_progress=True)
```

<p>&nbsp;</p>

<div dir="rtl" align="right">

# دریافت سابقه روزانه شاخص‌های بازار بورس
<hr style="border:2px solid gray"> </hr>


### : دریافت سابقه شاخص کل

</div>

```python
fpy.Get_CWI_History(
    start_date='1395-01-01',
    end_date='1400-12-29',
    ignore_date=False,
    just_adj_close=False,
    show_weekday=False,
    double_date=False)
```

<div dir="rtl" align="right">

### : دریافت سابقه شاخص کل هم‌وزن

</div>

```python
fpy.Get_EWI_History(
    start_date='1395-01-01',
    end_date='1400-12-29',
    ignore_date=False,
    just_adj_close=True,
    show_weekday=False,
    double_date=False)
```

<div dir="rtl" align="right">

### : دریافت سابقه شاخص قیمت وزنی-ارزشی

</div>

```python
fpy.Get_CWPI_History(
    start_date='1395-01-01',
    end_date='1400-12-29',
    ignore_date=False,
    just_adj_close=False,
    show_weekday=False,
    double_date=False)
```

<div dir="rtl" align="right">

### : دریافت سابقه شاخص قیمت هم‌وزن

</div>

```python
fpy.Get_EWPI_History(
    start_date='1395-01-01',
    end_date='1400-12-29',
    ignore_date=False,
    just_adj_close=False,
    show_weekday=False,
    double_date=False)
```

<div dir="rtl" align="right">

### : دریافت سابقه شاخص سهام آزاد شناور
</div>

```python
fpy.Get_FFI_History(
    start_date='1395-01-01',
    end_date='1400-12-29',
    ignore_date=False,
    just_adj_close=False,
    show_weekday=False,
    double_date=False)
```

<div dir="rtl" align="right">

### : دریافت سابقه شاخص بازار اول

</div>

```python
fpy.Get_MKT1I_History(
    start_date='1395-01-01',
    end_date='1400-12-29',
    ignore_date=False,
    just_adj_close=False,
    show_weekday=False,
    double_date=False)
```

<div dir="rtl" align="right">

### : دریافت سابقه شاخص بازار دوم

</div>

```python
fpy.Get_MKT2I_History(
    start_date='1395-01-01',
    end_date='1400-12-29',
    ignore_date=False,
    just_adj_close=False,
    show_weekday=False,
    double_date=False)
```

<div dir="rtl" align="right">

### : دریافت سابقه شاخص صنعت

</div>

```python
fpy.Get_INDI_History(
    start_date='1395-01-01',
    end_date='1400-12-29',
    ignore_date=False,
    just_adj_close=False,
    show_weekday=False,
    double_date=False)
```

<div dir="rtl" align="right">

### : دریافت سابقه شاخص 50 شرکت فعال‌تر
</div>

```python
fpy.Get_ACT50_History(
    start_date='1395-01-01',
    end_date='1400-12-29',
    ignore_date=False,
    just_adj_close=False,
    show_weekday=False,
    double_date=False)
```

<div dir="rtl" align="right">

### : دریافت سابقه شاخص 30 شرکت بزرگ

</div>

```python
fpy.Get_LCI30_History(
    start_date='1395-01-01',
    end_date='1400-12-29',
    ignore_date=False,
    just_adj_close=False,
    show_weekday=False,
    double_date=False)
```

<div dir="rtl" align="right">

### : دریافت سابقه شاخص صنایع بورسی

</div>

```python
fpy.Get_SectorIndex_History(
    sector='خودرو',
    start_date='1395-01-01',
    end_date='1400-12-29',
    ignore_date=False,
    just_adj_close=False,
    show_weekday=False,
    double_date=False)
```

<p>&nbsp;</p>

<div dir="rtl" align="right">

# اطلاعات لحظه‌ای بازار
<hr style="border:2px solid gray"> </hr>


### : دریافت اطلاعات لحظه‌ای بازار

</div>

```python
fpy.Get_MarketWatch(
    save_excel=True,
    save_path='D:/FinPy-TSE Data/MarketWatch')
```

<p>&nbsp;</p>

<div dir="rtl" align="right">

# دانلود دسته‌جمعی و پنل قیمت
<hr style="border:2px solid gray"> </hr>


### : دریافت لیست جامع سهم‌ها

</div>

```python
fpy.Build_Market_StockList(
    bourse=True,
    farabourse=True,
    payeh=True,
    detailed_list=True,
    show_progress=True,
    save_excel=True,
    save_csv=True,
    save_path='D:/FinPy-TSE Data/')
```

<div dir="rtl" align="right">

### : دانلود دسته‌جمعی اطلاعات و ساخت پنل قیمت

</div>

```python
fpy.Build_PricePanel(
    stock_list,
    jalali_date=True,
    save_excel=True,
    save_path='D:/FinPy-TSE Data/Price Panel/')
```

<p>&nbsp;</p>

<div dir="rtl" align="right">

# دلار آمریکا
<hr style="border:2px solid gray"> </hr>


### : دسترسی به سابقه روزانه قیمت دلار

</div>

```python
fpy.Get_USD_RIAL(
    start_date='1395-01-01',
    end_date='1400-12-29',
    ignore_date=False,
    show_weekday=False,
    double_date=False)
```
