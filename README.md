<h1>On Target Football Shop</h1>
<h3>On Target Football Shop adalah toko terbaik untuk mencari peralatan persepakbolaan Anda!</h3>
<br>
<h4>Link Deployment : https://erico-putra-ontargetfootballshop.pbp.cs.ui.ac.id/</h4>
<br>

<h2>Tugas 2</h2>
<ul>
  <li>
    <ol>
      <li>
        Cara saya mengimplementasikan checklist tugas untuk membangun kerangka dasar dari website e-commerce ini pertama - tama adalah dengan membuat sebuah repository github untuk menampung git dari proyek ini.  Dalam pembuatan proyek website, saya cukup terbiasa untuk membuat repository github terlebih dahulu karena akan mempermudah saya untuk langsung melakukan commit dan push.
      </li>
      <li>
        Setelah melakukan pembuatan repository github, hal yang saya lakukan adalah membuat folder sebagai tempat dimana saya akan membangun proyek website ini, dan membukanya melalui code editor yang saya cintai yakni VSCode. Di dalam folder ini, saya menginisiasi terminal (Powershell), dan menghubungkan proyek local saya menuju ke repository github yang telah saya buat sebelumnya.
      </li>
      <li>
        Setelah itu, saya menginisiasi python virtual environment melalui terminal yang telah saya buka sebelumnya. Tujuan dari diciptakannya python virtual environment ini utamanya adalah untuk menjaga dari konflik - konflik yang tidak diinginkan selama pembangunan proyek.
      </li>
      <li>
        File yang bernama requirements.txt kemudian saya buat, dan di dalamnya saya isikan berbagai dependencies yang berguna untuk pembuatan proyek website, termasuk juga di dalamnya adalah web framework untuk bahasa pemrograman Python yakni adalah Django. Melalui terminal, saya lakukan instalasi dependencies yang telah saya tulis.
      </li>
      <li>
        Setelah proses instalasi selesai, saya menginisiasi proyek django yang saya namai On_Target (diambil dari nama website yang saya bangun ini). 
      </li>
      <li>
        Setelahnya, saya membuat dua buah file yakni .env dan .env.prod dimana .env. Di dalam .env (untuk pengembangan secara local), saya atur PRODUCTION=FALSE, dan di dalam .env.prod (untuk deployment) saya atur PRODUCTION=TRUE dan saya sertakan pula kredensial database yang akan saya gunakan dalam proyek ini.
      </li>
      <li>
        Sebagai imbas dari implementasi file .env dan .env.prod pada step sebelumnya, maka saya perlu melakukan pengaturan pada file settings.py sebagai "pusat kendali" dari proyek ini. Saya perlu melakukan import library dotenv untuk mengatur lebih lanjut mengenai environment database. Pada settings.py, saya melakukan sedikit modifikasi pada pengaturan database, dimana ketika proses production deployment, maka proyek akan menggunakan database PostgreSQL yang disediakan oleh Fasilkom, dan selama proses development kita akan menggunakan database SQLite.
      </li>
      <li>
        Setelah itu, saya melakukan migration pada proyek Django yang saya buat.
      </li>
      <li>
        Kemudian, saya membuat file .gitignore yang berisikan hal - hal yang harus diabaikan oleh git ketika proses commit dan push. Hal ini bertujuan untuk menjaga file - file krusial yang sifatnya rahasia, seperti contohnya adalah kredensial.
      </li>
      <li>
        Setelahnya, saya menyimpan progress pengembangan dengan melakukan commit dan push menuju repository github yang telah saya buat.
      </li>
      <li>
        Setelah semua step diatas saya lakukan, saya menginisiasi aplikasi baru yang saya nama 'main', dan saya daftarkan aplikasi 'main' yang saya buat ke dalam INSTALLED_APPS pada settings.py.
      </li>
      <li>
        Dalam models.py, saya tambahkan beberapa atribut produk yang nantinya tampil dalam website saya. Atribut - atribut tersebut saya daftarkan di dalam sebuah dalam model class yang bernama Product.
      </li>
      <li>
        Karena saya melakukan perubahan pada models.py, maka untuk kedua kalinya saya melakukan migration.
      </li>
      <li>
        Kemudian, saya mengoordinasikan file moduls.py, views.py, dan urls.py supaya dapat menampilkan isi dari main.html yang saya buat di dalam file templates. Objektifnya adalah untuk membentuk routing yang benar, dan membuat data yang ditampilkan pada template main.html dapat dimanipulasi melalui models.py dan views.py (supaya tidak lagi hardcode melalui file main.html)
      </li>
      <li>
        Setelah melakukan semua step diatas, akhirnya saya melakukan deployment melalui Pacil Web Server, dan website pun berjalan dengan baik.
      </li>
    </ol>
  </li>
  <br>
  <li>
      <img width="711" height="295" alt="image" src="https://github.com/user-attachments/assets/38066383-6859-420b-85ec-ee4c4a4b411b" />
      <h5>
        Dalam framework website Django, digunakan alur kerja MVT (Model-View-Template) seperti bagaimana tergambar pada grafik yang saya gambarkan. View akan menerima request (umumnya berupa URL) dan kemudian ia akan menentukan apakah akan diteruskan menuju ke models, atau langsung menuju interface (template). Apabila perlu dilakukan pengolahan data terlebih dahulu, maka request akan diproses menuju models dan terjadi pengambilan data dari database apabila diperlukan. Setelah pemrosesan dalam models, maka request akan dikembalikan menuju Views dan diteruskan menuju template. Terakhir, tampilan akan dikembalikan dalam bentuk response dan dikembalikan oleh Templates melalui Views. Secara garis besar dan dengan pengistilahan yang cukup disederhanakan, begitulah cara kerja MVT pada framework website Django.
      </h5>
  </li>                        
  <br>
  <li>
    Peran settings.py dalam proyek Django adalah sebagai "pusat kendali" dari proyek Django tersebut. Seperti proyek pada umumnya, diperlukan suatu entitas yang berperan sebagai pusat kendali untuk memonitor dan menjaga proyek untuk berjalan lancar. Pada file settings.py, kita dapat mengatur beberapa hal yang krusial dalam proyek Django, seperti contohnya pengaturan database.
  </li>
  <br>
  <li>
    Pada dasarnya, migrations perlu dilakukan ketika kita melakukan modifikasi pada models supaya database dapat menyesuaikan perubahan yang dilakukan. Django memiliki sebuah folder yang menyimpan riwayat migrations yang pernah dilakukan. Setiap kali terjadi kita melakukan migrations, maka Django akan membandingkan isi dari models dengan riwayat migrations yang pernah dilakukan. Apabila ditemukan suatu perubahan, maka django akan melakukan migrations, melakukan adjustment pada database, dan mencatatnya dalam folder riwayat migrations. Dengan bahasa yang sedikit oversimplified, kurang lebih seperti itulah cara kerja dari migrations pada django framework.
  </li>
  <br>
  <li>
    Menurut saya, dipilihnya framework Django bertujuan untuk memberikan pengetahuan mengenai salah satu alur kerja website development yang cukup populer, yakni adalah Model View Template. Selain itu, django framework menggunakan bahasa pemrograman Python yang selaras dengan bahasa pemrograman pengantar pada mata kuliah prasyarat PBP, yakni Dasar - Dasar Pemrograman 1. Django juga merupakan salah satu framework website yang cukup banyak digunakan di dunia dalam ranah pengembangan perangkat lunak website.
  </li>
  <br>
  <li>
    Seluruh staf dosen dan asisten dosen menurut saya sudah cukup melakukan pekerjaan dengan cukup baik! Terima kasih para asisten dosen dan tim dosen sekalian!
  </li>

<br>
<h2>Tugas 3</h2>
<ul>
  <li>
    Dalam implementasi sebuah platform, kita memerlukan data delivery untuk membuat platform tersebut menjadi lebih interaktif dan dinamis. Hal tersebut karena data delivery menyajikan mekanisme untuk memastikan data dapat berpindah dari suatu komponen ke komponen lainnya dengan cepat, aman, dan konsisten.
  </li>
  <li>
    JSON dapat dikatakan lebih populer dibandingkan XML karena JSON dapat dengan mudah digunakan dalam JavaScript tanpa harus melakukan parsing yang rumit. Dalam pengembangan perangkat lunak, JavaScript sangat umum digunakan untuk mengolah data dalam suatu platform.
  </li>
  <li>
    Method is_valid() dalam suatu proyek Django merupakan hal yang penting, karena method tersebut bertugas untuk mengecek apakah semua field - field yang telah dimasukkan oleh user sudah memenuhi syarat yang telah dicantumkan pada models.py. Jika telah memenuhi syarat, maka Django akan menerima request POST kita. Sebaliknya, jika tidak memenuhi syarat, maka Django akan mendeteksi hal tersebut sebagai kesalahan input  dan kemudian akan memberikan error message.
  </li>
  <li>
    Pengadaan CSRF Token merupakan hal yang sangat penting bagi keamanan perangkat lunak yang kita bangun. Ketika kita mengakses perangkat lunak berbasis Django, maka Django akan membuat suatu token unik per sesi yang disisipkan dalam setiap form POST. Jika cocok, maka request akan dianggap valid. Jika tidak cocok, maka terjadi error 403 (Forbidden). CSRF Token sangat penting terutama untuk menghindari CSRF attack.
  </li>
  <li>
    <ol>
      <li>
        Pertama, saya membuat sebuah file baru pada directory /main yakni forms.py. File python ini berfungsi untuk mengatur form input data dan mendeklarasikan field - field yang akan dijadikan input nantinya.
      </li>
      <li>
        Kemudian, saya menambahkan beberapa template untuk tampilan yang lebih dinamis ketika kita menambahkan product, atau melihat detail dari product yang kita tambahkan. Dalam direktori /main/templates, saya menambahkan create_product.html sebagai tampilan ketika kita ingin menambahkan product, dan product_detail.html ketika kita ingin melihat detail product yang telah kita tambahkan.
      </li>
      <li>
        Kemudian, pada views.py, saya membuat sebuah fungsi create_product() yang memiliki parameter request. Fungsi ini bertugas untuk menambahkan produk yang telah diinputkan oleh user, dan mengecek validitas input yang diberikan oleh user. Apabila input sesuai dengan syarat yang diberikan pada models.py, maka request POST akan disetujui. Apabila input tidak sesuai dengan syarat yang diberikan pada models.py, maka request POST akan ditolak.
      </li>
      <li>
        Kemudian, pada views.py, saya membuat sebuah fungsi yang bernama show_product(). Fungsi ini berisi seluruh product yang telah dimasukkan, dan nantinya akan diiterasikan pada template yang telah dibuat supaya user dapat melihat product apa saja yang telah ditambahkan.
      </li>
      <li>
        Kemudian, saya membuat beberapa fungsi seperti show_xml_by_id(), show_json_by_id() sebagai fungsi yang akan memberikan output data product yang telah ditambahkan masing-masing dalam bentuk format XML dan JSON.
      </li>
    </ol>
  </li>
  <li>
    Asdos semua sudah keren!
  </li>
  <li>
    Berikut ini saya lampirkan foto hasil akses URL pada Postman : 
    <ol>
      <li>
        JSON
        <img width="1380" height="922" alt="image" src="https://github.com/user-attachments/assets/0d0b1b33-7751-41ad-922b-c8228dda1caa" />
      </li>
      <li>
        XML
        <img width="1385" height="958" alt="image" src="https://github.com/user-attachments/assets/e73bb1be-ca27-47f6-88e1-6def8c5d17cb" />
      </li>
    </ol>
  </li>
</ul>

<br>
<h2>Tugas 5</h2>
<ul>
  <li>Urutan CSS Selector mulai dari hierarki paling tinggi adalah :</li>
  <ol>
    <li>
      !important akan mengalahkan semua prioritas. Akan tetapi, penggunaannya haruslah secara bijak.
    </li>
    <li>
      Inline-style. Karena kode CSS dengan penulisan inline-style langsung ditulis didalam file HTML, sehingga ia mendapat prioritas paling utama.
    </li>
    <li>
      External CSS :  Jika tidak terdapat kode CSS inline pada file HTML, maka akan digunakan kode yang terdapat pada external CSS (jika ada juga). Pada kode external CSS tersebut, ID selector menjadi prioritas utama, diikuti dengan class, attribute, element, pseudo-element.
    </li>
    <li>
      Responsive design menjadi sangat penting di era saat ini karena pada era saat ini, ada sangat amat beragam jenis ukuran layar daripada device yang dimiliki oleh para user. Dengan membuat responsive design, maka website akan bisa menyesuaikan dengan ukuran layar yang dimiliki oleh para user, sehingga akan meningkatkan pengalaman user.
    </li>
  </ol>
  
  <li>
      Margin adalah memberikan space sebesar nilai tertentu DILUAR elemen pembungkusnya. 
  </li>
  <li>
      Padding adalah memberikan space sebesar nilai tertentu DIDALAM elemen pembungkusnya.
  </li>
  <li>
      Border adalah garis tepi yang bentuknya mengikuti bentuk elemen pembungkus.
  </li>
  <li>
    <ul>
      <li>
        Flexbox adalah design yang terfokus pada mengatur desain dari sisi satu dimensi saja, baik itu secara vertikal (column) dan horizontal (row)
      </li>
      <li>
        Gridbox adalah design yang terfokus pada pengaturan desain dari sisi dua dimensi, sehingga kita bisa mengatur dari sisi baris maupun kolom sekaligus.
      </li>
    </ul>
  </li>
  <li>
    Proses pengerjaan yang saya lakukan mengikuti apa yang terdapat pada tutorial 4.
  </li>
</ul>
