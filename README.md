<h1>On Target Football Shop</h1>
<h3>On Target Football Shop adalah toko terbaik untuk mencari peralatan persepakbolaan Anda!</h3>
<br>
<h4>Link Deployment : https://erico-putra-ontargetfootballshop.pbp.cs.ui.ac.id/</h4>
<br>
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
  </li>
    
  </li>>
