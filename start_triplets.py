import pandas as pd

# Triplet data
triplets = [
    (
        "IHSG melemah karena kekhawatiran inflasi global",
        "Kenaikan inflasi AS menekan pasar Asia, termasuk Indonesia",
        "IHSG adalah istilah dalam buku pelajaran ekonomi"
    ),
    (
        "IHSG naik usai rilis data cadangan devisa",
        "BI mengumumkan cadangan devisa Indonesia meningkat",
        "Data cuaca terbaru menunjukkan musim hujan tertunda"
    ),
    (
        "Investor asing melakukan aksi jual di pasar saham",
        "Penurunan IHSG dipicu oleh capital outflow",
        "Investor sedang ramai membahas crypto di TikTok"
    ),
    (
        "IHSG ditutup menguat seiring penguatan rupiah",
        "Rupiah menguat terhadap dolar AS setelah BI menaikkan suku bunga",
        "IHSG adalah indeks yang diajarkan di kelas ekonomi"
    ),
    (
        "IHSG bergerak melemah setelah pidato The Fed",
        "Komentar Jerome Powell membuat pasar global bergejolak",
        "IHSG kadang digunakan dalam soal pilihan ganda"
    ),
    (
        "IHSG rebound setelah sentimen positif dari Wall Street",
        "Pasar saham Asia ikut menguat mengikuti rally di Wall Street",
        "IHSG merupakan singkatan yang populer di media sosial"
    ),
    (
        "IHSG terkoreksi akibat data inflasi domestik yang tinggi",
        "Inflasi Indonesia bulan ini tercatat 4,2%, lebih tinggi dari ekspektasi",
        "IHSG sering digunakan dalam skripsi mahasiswa ekonomi"
    ),
    (
        "IHSG stabil meskipun harga minyak melonjak",
        "Harga minyak mentah dunia naik akibat ketegangan geopolitik",
        "Minyak goreng naik harga di pasar tradisional"
    ),
    (
        "Kinerja emiten perbankan menopang penguatan IHSG",
        "Laba bersih Bank Mandiri naik signifikan kuartal ini",
        "IHSG adalah topik dalam ujian nasional"
    ),
    (
        "IHSG melemah setelah keluarnya investor asing",
        "Net sell asing mencapai Rp1 triliun hari ini",
        "IHSG hanya dikenal oleh ekonom dan pengusaha"
    ),
    (
        "IHSG ditutup melemah 0,7% pada perdagangan hari Senin akibat kekhawatiran investor terhadap potensi resesi global.",
        "Kekhawatiran resesi global dan pengetatan kebijakan moneter oleh The Fed membuat indeks saham di kawasan Asia turut terkoreksi.",
        "Harga cabai merah di pasar tradisional mengalami lonjakan hingga 30% menjelang libur panjang."
    ),
    (
        "Penguatan IHSG hari ini didorong oleh aksi beli investor asing pada saham-saham blue chip sektor perbankan.",
        "Saham Bank BCA dan BRI menjadi penopang utama penguatan indeks setelah mencatatkan kenaikan volume transaksi signifikan.",
        "Sebagian besar wisatawan lokal memilih destinasi pegunungan untuk menghindari cuaca panas ekstrem."
    ),
    (
        "IHSG rebound setelah tiga hari berturut-turut melemah, didorong sentimen positif dari kenaikan cadangan devisa dan stabilnya nilai tukar rupiah.",
        "Bank Indonesia mencatat kenaikan cadangan devisa sebesar USD 3 miliar, memberikan sinyal positif bagi pelaku pasar.",
        "Festival budaya di Solo menghadirkan puluhan penari tradisional dari berbagai daerah."
    ),
    (
        "IHSG bergerak fluktuatif sepanjang hari seiring pelaku pasar menanti keputusan suku bunga dari Bank Sentral Eropa.",
        "Pasar saham global bergerak mixed dengan volume transaksi tipis, menandakan sikap wait and see dari para investor.",
        "Komunitas penggemar bonsai menggelar pameran tanaman hias langka di Jakarta Selatan."
    ),
    (
        "Pelemahan IHSG kali ini didorong oleh aksi profit taking setelah penguatan tajam selama dua pekan terakhir.",
        "Analis menilai aksi ambil untung wajar terjadi mengingat valuasi beberapa saham big cap sudah mencapai level tertinggi tahun ini.",
        "Banjir yang melanda sejumlah wilayah di Jawa Tengah mengganggu aktivitas pertanian lokal."
    ),
    (
        "IHSG naik tipis di tengah kekhawatiran pasar terhadap potensi kebijakan fiskal baru pasca pelantikan kabinet baru.",
        "Investor masih mencermati arah kebijakan ekonomi presiden terpilih yang dinilai akan berdampak pada kinerja pasar modal.",
        "Penerbitan novel fiksi ilmiah terbaru dari penulis lokal menarik perhatian komunitas pembaca remaja."
    ),
    (
        "IHSG terkoreksi akibat pelemahan sektor komoditas menyusul penurunan harga batu bara dan minyak dunia.",
        "Harga minyak mentah jenis Brent turun lebih dari 5% setelah rilis data persediaan AS yang lebih tinggi dari ekspektasi.",
        "Cuaca cerah diperkirakan akan berlangsung hingga akhir pekan di sebagian besar wilayah Jawa."
    ),
    (
        "Meskipun pasar global melemah, IHSG tetap menguat karena dorongan sektor infrastruktur yang mencatatkan lonjakan transaksi.",
        "Saham-saham konstruksi dan properti melonjak setelah pemerintah mengumumkan percepatan proyek IKN tahap kedua.",
        "Pendaftaran peserta lomba lari maraton nasional telah dibuka dan berlangsung hingga akhir bulan."
    ),
    (
        "IHSG berada di zona hijau berkat ekspektasi positif terhadap laporan keuangan kuartal ketiga sejumlah emiten besar.",
        "Emiten sektor perbankan dan telekomunikasi diprediksi membukukan pertumbuhan laba dobel digit pada Q3.",
        "Museum nasional merilis koleksi arkeologi terbaru dari temuan situs di Kalimantan Timur."
    ),
    (
        "Penurunan IHSG disebabkan oleh gejolak geopolitik di Timur Tengah yang meningkatkan aversi risiko investor global.",
        "Ketegangan politik di kawasan Teluk menyebabkan harga komoditas melonjak dan arus dana keluar dari pasar berkembang.",
        "Komunitas pecinta reptil mengadakan gathering nasional dengan berbagai kontes hewan eksotik."
    ),
        (
        "IHSG mengalami koreksi tajam setelah rilis data inflasi yang lebih tinggi dari perkiraan analis.",
        "Data inflasi nasional menunjukkan lonjakan harga pangan yang signifikan, memicu kekhawatiran di pasar modal.",
        "Pameran seni lukis kontemporer digelar di pusat kebudayaan selama satu minggu penuh."
    ),
    (
        "Lonjakan IHSG hari ini dipicu oleh penguatan rupiah terhadap dolar Amerika Serikat.",
        "Nilai tukar rupiah yang stabil cenderung meningkatkan minat investor asing di pasar saham domestik.",
        "Tim sepak bola nasional berhasil meraih kemenangan telak dalam laga persahabatan internasional."
    ),
    (
        "IHSG mencatat rekor tertinggi bulanan setelah sentimen positif dari rilis laporan keuangan emiten teknologi.",
        "Saham sektor teknologi menguat setelah beberapa perusahaan membukukan kinerja kuartalan yang di atas ekspektasi.",
        "Peluncuran smartphone terbaru menarik perhatian pecinta gadget di seluruh Indonesia."
    ),
    (
        "Aksi beli investor lokal berhasil menahan laju penurunan IHSG akibat tekanan eksternal dari pasar global.",
        "Keterlibatan investor domestik meningkat saat tekanan eksternal menciptakan gejolak di bursa saham.",
        "Lalu lintas di jalur Puncak padat merayap sejak pagi akibat libur panjang akhir pekan."
    ),
    (
        "IHSG masih berada dalam tren konsolidasi karena pelaku pasar menunggu kepastian arah kebijakan suku bunga.",
        "Investor cenderung wait and see menjelang pengumuman suku bunga dari otoritas moneter minggu depan.",
        "Turnamen e-sports nasional berlangsung meriah dengan peserta dari berbagai provinsi."
    ),
    (
        "Perdagangan IHSG ditutup menguat berkat aksi akumulasi saham sektor energi dan konsumsi.",
        "Saham energi melonjak setelah harga minyak dunia naik tajam dalam sepekan terakhir.",
        "Pelatihan literasi digital bagi guru dilaksanakan di lima kota besar secara serentak."
    ),
    (
        "IHSG sempat melemah di sesi awal namun berhasil rebound menjelang penutupan perdagangan.",
        "Rebound indeks menjelang akhir sesi ditopang oleh penguatan sektor keuangan dan properti.",
        "Panen raya di desa terpencil membawa harapan baru bagi ketahanan pangan lokal."
    ),
    (
        "IHSG rentan terkoreksi karena ketidakpastian global dan meningkatnya kasus COVID-19 di kawasan Asia.",
        "Lonjakan kasus COVID-19 di beberapa negara Asia membuat pasar saham regional melemah.",
        "Pertunjukan wayang kulit digelar semalam suntuk untuk memperingati hari jadi desa."
    ),
    (
        "Kinerja IHSG hari ini ditopang oleh sentimen positif pasca diumumkannya data surplus neraca dagang.",
        "Surplus perdagangan Indonesia mendorong optimisme pelaku pasar terhadap fundamental ekonomi.",
        "Komunitas sepeda mengadakan tur keliling kota sebagai bagian dari kampanye lingkungan."
    ),
    (
        "IHSG dibuka menguat tipis di tengah minimnya sentimen global dan rilis data ekonomi yang netral.",
        "Minimnya sentimen eksternal membuat pergerakan indeks cenderung terbatas sejak pagi.",
        "Kegiatan outbound untuk siswa sekolah dasar diadakan di kawasan wisata alam lokal."
    ),
    (
        "IHSG ditutup menguat 1,2% ke level 7.056 pada perdagangan hari Selasa, didorong oleh sentimen positif dari penguatan saham sektor perbankan dan energi, serta masuknya dana asing sebesar Rp 1,3 triliun.",
        "Penguatan IHSG hari ini mencerminkan respons positif pelaku pasar terhadap stabilnya kurs rupiah dan menguatnya harga komoditas global, terutama batu bara dan minyak mentah.",
        "Festival kuliner nusantara dibuka hari ini di Lapangan Banteng dengan menghadirkan lebih dari 150 UMKM dari seluruh Indonesia."
    ),
    (
        "Kinerja indeks harga saham gabungan (IHSG) sepanjang pekan ini mengalami tekanan akibat meningkatnya tensi geopolitik di kawasan Eropa Timur, yang mendorong investor beralih ke aset safe haven seperti emas.",
        "Peningkatan ketegangan antara Rusia dan Ukraina turut menekan pasar regional, dengan IHSG terkoreksi 0,9% dalam lima hari perdagangan terakhir meski sektor telekomunikasi sempat menopang indeks.",
        "Konser musik rock terbesar tahun ini sukses digelar di Gelora Bung Karno dan menarik puluhan ribu penonton dari berbagai kota."
    ),
    (
        "IHSG dibuka melemah tipis pagi ini seiring rilis data pertumbuhan ekonomi kuartal kedua Indonesia yang berada di bawah ekspektasi analis, yaitu 4,9% dibandingkan estimasi konsensus sebesar 5,1%.",
        "Pelaku pasar merespons negatif terhadap data PDB yang lebih rendah karena dianggap mencerminkan pemulihan ekonomi yang masih melambat, khususnya di sektor konsumsi dan industri manufaktur.",
        "Komunitas astronomi lokal mengadakan pengamatan hujan meteor di lereng Gunung Merbabu malam ini."
    ),
    (
        "Saham-saham sektor konstruksi menjadi penopang utama penguatan IHSG hari ini setelah pemerintah mengumumkan paket percepatan proyek Ibu Kota Nusantara (IKN), termasuk pembangunan infrastruktur jalan dan jembatan tahap kedua.",
        "IHSG naik 0,65% ke level 6.994, ditopang oleh aksi beli investor domestik di saham PT PP, WIKA, dan Adhi Karya yang masing-masing mencatat lonjakan harga lebih dari 5% dalam sehari.",
        "Mahasiswa dari seluruh Indonesia mengikuti lomba debat nasional yang diselenggarakan secara daring oleh Kemendikbud."
    ),
    (
        "Pergerakan IHSG saat ini memasuki fase konsolidasi setelah sempat menembus resistance teknikal di level 7.000, di mana investor tengah menanti kepastian arah kebijakan moneter dari Bank Indonesia dan The Fed.",
        "Analis menilai bahwa volume transaksi yang mulai menipis serta indikator RSI yang mendekati area overbought mengindikasikan potensi koreksi teknikal dalam jangka pendek.",
        "Pemerintah daerah menggelar program vaksinasi rabies gratis untuk hewan peliharaan di 15 kecamatan."
    ),
    (
        "IHSG turun tajam sebesar 2,1% dalam sehari setelah Bank Sentral Amerika Serikat (The Fed) mengumumkan kenaikan suku bunga acuan sebesar 75 basis poin, memicu arus keluar modal dari pasar negara berkembang.",
        "Investor cenderung melakukan risk-off setelah pengumuman The Fed tersebut, dengan saham-saham berkapitalisasi besar di sektor teknologi dan keuangan menjadi yang paling terdampak.",
        "Acara peluncuran komik digital terbaru karya seniman lokal dihadiri oleh komunitas kreatif dari berbagai kota."
    ),
    (
        "Dalam lima tahun terakhir, tren pergerakan IHSG menunjukkan kecenderungan meningkat pada kuartal ketiga tiap tahunnya, terutama didorong oleh belanja pemerintah dan rilis kinerja emiten yang lebih baik pada semester pertama.",
        "IHSG cenderung mencetak return positif pada Q3 karena faktor musiman seperti realisasi anggaran belanja infrastruktur serta distribusi dividen interim dari beberapa perusahaan publik.",
        "Penerbitan kartu pra-kerja gelombang terbaru diumumkan hari ini oleh pemerintah melalui siaran langsung daring."
    ),
    (
        "IHSG ditutup menguat di tengah lonjakan volume transaksi yang mencapai Rp 15,2 triliun, tertinggi dalam dua bulan terakhir, menandakan peningkatan optimisme pelaku pasar terhadap kondisi makroekonomi nasional.",
        "Lonjakan volume tersebut sebagian besar berasal dari aksi beli pada saham sektor konsumer dan tambang, yang keduanya mendapatkan sentimen positif dari penguatan harga komoditas dan kenaikan daya beli masyarakat.",
        "Pengurus masjid besar kota mengadakan pelatihan marbot dalam rangka peningkatan layanan ibadah di bulan Ramadan."
    ),
    (
        "Indeks Harga Saham Gabungan (IHSG) berada dalam tekanan sepanjang sesi perdagangan akibat kekhawatiran pasar terhadap potensi gagal bayar utang luar negeri oleh salah satu BUMN besar yang bergerak di sektor energi.",
        "Kabar mengenai kemungkinan default dari entitas milik negara tersebut membuat investor asing melakukan aksi jual bersih senilai lebih dari Rp 900 miliar dalam satu hari.",
        "Perayaan Cap Go Meh tahun ini berlangsung meriah dengan atraksi barongsai di sepanjang jalan utama kota."
    ),
    (
        "IHSG kembali mencetak rekor intraday tertinggi tahun ini di level 7.134 setelah sentimen positif dari penguatan neraca transaksi berjalan serta penurunan rasio utang terhadap PDB Indonesia.",
        "Stabilitas fundamental makroekonomi dan kenaikan rating kredit Indonesia oleh lembaga internasional turut menopang kepercayaan investor terhadap pasar modal domestik.",
        "Dinas perhubungan meluncurkan sistem e-ticketing baru untuk seluruh layanan angkutan umum kota."
    ),
    (
        "IHSG bergerak fluktuatif sepanjang sesi perdagangan hari ini akibat tarik-menarik antara tekanan eksternal dari pelemahan bursa global dan sentimen domestik yang relatif stabil.",
        "Meskipun pasar regional mengalami tekanan, IHSG masih menunjukkan ketahanan berkat optimisme terhadap fundamental ekonomi dalam negeri.",
        "Komunitas fotografi mengadakan lomba potret lanskap alam terbuka dengan tema 'Keindahan Nusantara'."
    ),
    (
        "Saham sektor perbankan memimpin penguatan IHSG setelah Bank Indonesia mempertahankan suku bunga acuan pada level 6,25%, yang dinilai mendukung likuiditas pasar.",
        "Investor menilai kebijakan suku bunga yang akomodatif akan memberikan ruang tumbuh bagi perbankan dalam menyalurkan kredit secara lebih agresif.",
        "Festival tari tradisional digelar di alun-alun kota untuk memperingati hari jadi kabupaten."
    ),
    (
        "IHSG mencatat net sell asing selama tiga hari berturut-turut dengan total mencapai Rp 2,1 triliun, mencerminkan sentimen risk-off global akibat ketegangan perdagangan AS–Tiongkok yang memanas kembali.",
        "Aksi jual asing terlihat paling signifikan di saham-saham blue chip seperti BBCA, TLKM, dan ASII yang memiliki eksposur tinggi terhadap ekonomi global.",
        "Sekolah dasar negeri di Jawa Timur mengadakan pelatihan penanggulangan bencana untuk murid kelas 5 dan 6."
    ),
    (
        "Tekanan terhadap IHSG pada sesi penutupan disebabkan oleh pelemahan harga batu bara global yang menurunkan kinerja saham emiten energi seperti ADRO, PTBA, dan ITMG.",
        "Koreksi pada sektor energi menyeret indeks ke zona merah meskipun sektor konsumer mencatat penguatan moderat.",
        "Turnamen bola voli antar fakultas diselenggarakan oleh universitas dalam rangka dies natalis ke-60."
    ),
    (
        "IHSG rebound setelah rilis data cadangan devisa yang naik ke USD 138 miliar, memberikan kepercayaan pasar terhadap stabilitas neraca eksternal Indonesia.",
        "Kenaikan cadangan devisa dinilai mampu menopang nilai tukar rupiah dan memperkuat daya tahan pasar modal terhadap gejolak global.",
        "Pagelaran musik jazz di taman kota menarik ribuan penonton pada akhir pekan lalu."
    ),
    (
        "Pelaku pasar cenderung wait and see menjelang rilis laporan keuangan emiten kuartal kedua, yang menjadi penentu arah pergerakan IHSG dalam waktu dekat.",
        "Minat beli investor melemah karena ketidakpastian terhadap kinerja sektor properti dan otomotif yang diprediksi masih tertekan oleh suku bunga tinggi.",
        "Lembaga filantropi lokal menyalurkan bantuan sembako kepada warga terdampak banjir bandang."
    ),
    (
        "IHSG dibuka stagnan di awal pekan dengan volume perdagangan yang rendah karena pasar menantikan arahan kebijakan moneter global dari simposium tahunan Jackson Hole.",
        "Perdagangan yang sepi mencerminkan sikap hati-hati investor terhadap potensi hawkish statement dari Federal Reserve terkait inflasi AS.",
        "Pameran bonsai nasional menampilkan lebih dari 500 koleksi tanaman dari berbagai komunitas penghobi."
    ),
    (
        "Kinerja IHSG membaik seiring sentimen positif dari data Purchasing Managers Index (PMI) sektor manufaktur Indonesia yang kembali masuk ke zona ekspansi.",
        "PMI di atas 50 menunjukkan pertumbuhan aktivitas industri yang direspons positif oleh pelaku pasar saham, khususnya di sektor bahan baku dan industri berat.",
        "Perpustakaan keliling mulai beroperasi kembali setelah dua tahun vakum selama masa pandemi COVID-19."
    ),
    (
        "Emiten BUMN konstruksi menjadi penopang utama penguatan IHSG hari ini setelah kabar bahwa pemerintah akan menyuntikkan modal negara tambahan untuk percepatan proyek IKN.",
        "Saham seperti WIKA, PTPP, dan WSKT melonjak hingga batas atas (auto reject atas) karena lonjakan permintaan dari investor ritel dan institusi.",
        "Siswa SMP mengikuti kompetisi robotik nasional yang diselenggarakan di Jakarta Convention Center."
    ),
    (
        "IHSG turun tipis di tengah penguatan indeks bursa global, menunjukkan adanya divergensi sentimen domestik terkait potensi pelemahan daya beli akibat kenaikan harga BBM subsidi.",
        "Saham-saham sektor konsumer terpukul oleh ekspektasi inflasi yang lebih tinggi, terutama saham ritel dan barang konsumsi rumah tangga.",
        "Museum kota membuka pameran temporer tentang sejarah jalur perdagangan rempah-rempah di Nusantara."
    ),
    (
        "IHSG mengalami volatilitas tinggi pada sesi kedua setelah muncul spekulasi bahwa Bank Indonesia akan mempertimbangkan kenaikan suku bunga tambahan dalam waktu dekat.",
        "Isu pengetatan moneter tersebut memicu aksi ambil untung oleh investor jangka pendek, terutama di saham-saham lapis dua yang sebelumnya mencatat kenaikan signifikan.",
        "Tim futsal kampus meraih juara dua dalam kejuaraan nasional antar perguruan tinggi se-Indonesia."
    ),
    (
        "Kinerja IHSG pada awal kuartal keempat menunjukkan pola konsolidasi dengan kecenderungan melemah, seiring dengan tekanan dari depresiasi nilai tukar rupiah terhadap dolar AS.",
        "Investor asing melakukan aksi jual bersih sebesar Rp 1 triliun dalam seminggu terakhir karena meningkatnya ketidakpastian global terkait outlook suku bunga AS.",
        "Sekolah menengah kejuruan di Makassar mengadakan pameran hasil karya siswa bidang otomotif dan teknik mesin."
    ),
    (
        "IHSG kembali ditutup di zona merah setelah laporan inflasi Amerika Serikat menunjukkan angka yang lebih tinggi dari ekspektasi, meningkatkan ekspektasi bahwa The Fed akan tetap agresif.",
        "Data inflasi tersebut menyebabkan penguatan dolar dan pelemahan pasar saham global, termasuk di Indonesia, yang terdampak melalui outflow dana asing.",
        "Festival budaya Betawi digelar di Monas dengan rangkaian pertunjukan ondel-ondel dan lenong Betawi."
    ),
    (
        "Saham sektor teknologi memimpin penguatan IHSG di tengah optimisme pelaku pasar terhadap adopsi transformasi digital dan pertumbuhan ekonomi berbasis teknologi di Indonesia.",
        "Kinerja saham seperti BUKA dan GOTO mencatat rebound setelah tekanan sepanjang semester pertama, didorong oleh laporan keuangan yang menunjukkan penurunan kerugian operasional.",
        "Lembaga pelatihan kerja membuka program magang berbasis kompetensi digital untuk lulusan SMA dan SMK."
    ),
    (
        "IHSG bergerak menguat secara moderat pada awal sesi perdagangan seiring optimisme terhadap kelanjutan proyek-proyek strategis nasional menjelang akhir tahun anggaran.",
        "Analis memperkirakan sektor konstruksi dan bahan bangunan akan menjadi fokus utama investor karena prospek percepatan belanja infrastruktur pemerintah.",
        "Kompetisi masak makanan tradisional digelar oleh komunitas kuliner lokal untuk memperingati hari pangan sedunia."
    ),
    (
        "IHSG mendapat sentimen positif dari penguatan bursa Wall Street semalam, yang dipicu oleh meredanya kekhawatiran investor terhadap perlambatan ekonomi AS setelah rilis data tenaga kerja yang solid.",
        "Pelaku pasar menilai bahwa pemulihan ekonomi global akan berdampak positif terhadap permintaan ekspor Indonesia dan berpotensi menopang kinerja emiten berorientasi ekspor.",
        "Balai pelestarian cagar budaya meresmikan situs arkeologi baru di kawasan pesisir selatan Jawa."
    ),
    (
        "IHSG bergerak dalam rentang sempit menjelang libur panjang, dengan volume transaksi yang cenderung rendah dan dominasi aksi wait and see dari investor.",
        "Ketidakpastian arah pasar dalam jangka pendek mendorong investor institusi untuk memarkir dana di aset defensif seperti saham sektor utilitas dan konsumer primer.",
        "Badan meteorologi mengeluarkan peringatan dini gelombang tinggi di wilayah perairan selatan Jawa dan Bali."
    ),
    (
        "IHSG sempat menyentuh support teknikal di level 6.820 sebelum akhirnya ditutup menguat tipis, menunjukkan adanya minat beli di level bawah yang cukup kuat.",
        "Indikator stochastic dan MACD mulai menunjukkan potensi reversal bullish jangka pendek, terutama jika volume mulai meningkat pada sesi selanjutnya.",
        "Lomba desain batik digital diikuti oleh lebih dari 300 peserta dari berbagai SMA di Indonesia."
    ),
    (
        "Kinerja IHSG sepanjang bulan ini cukup stabil meskipun terdapat tekanan dari penurunan harga komoditas global seperti CPO dan nikel yang berdampak pada emiten sektor tambang.",
        "Sektor perbankan dan infrastruktur menjadi penyeimbang terhadap tekanan sektor komoditas, mencerminkan rotasi sektor oleh pelaku pasar domestik.",
        "Dinas kesehatan menggelar kampanye vaksinasi flu musiman di sekolah dasar dan puskesmas wilayah timur Jakarta."
    ),
    (
        "IHSG menguat pada pembukaan pekan ini berkat sentimen positif dari outlook pertumbuhan ekonomi Indonesia yang dipertahankan pada level 5% oleh lembaga pemeringkat internasional.",
        "Revisi naik outlook Indonesia ke 'stabil' turut meningkatkan daya tarik pasar modal nasional bagi investor global yang sedang melakukan alokasi ulang portofolio.",
        "Organisasi lingkungan hidup lokal meluncurkan program pelestarian mangrove di wilayah pesisir utara Semarang."
    ),
    (
        "IHSG dibuka melemah seiring kekhawatiran pasar terhadap potensi capital outflow akibat penguatan dolar AS dan meningkatnya imbal hasil obligasi global.",
        "Investor mulai mengalihkan portofolionya ke aset safe haven seperti emas dan surat utang negara, meninggalkan saham-saham berisiko tinggi.",
        "Tim seni tari dari SMA Negeri 5 Bandung tampil memukau dalam Festival Tari Tradisional tingkat provinsi."
    ),
    (
        "IHSG menunjukkan tren sideways sepanjang pekan terakhir menjelang pengumuman data inflasi domestik dan hasil rapat dewan gubernur Bank Indonesia.",
        "Ketidakpastian terhadap arah kebijakan moneter jangka pendek membuat investor ritel cenderung wait and see dan menahan diri untuk entry.",
        "Museum tekstil menggelar pameran khusus tentang sejarah batik tulis dari berbagai daerah di Indonesia."
    ),
    (
        "Tekanan jual di IHSG meningkat setelah lembaga pemeringkat menurunkan prospek utang global beberapa negara berkembang, memicu sentimen negatif di pasar emerging markets.",
        "Investor asing melakukan aksi jual bersih yang cukup agresif terutama di sektor energi dan perbankan yang memiliki eksposur global.",
        "Komunitas astronomi lokal mengadakan pengamatan gerhana bulan sebagian di kawasan Puncak Bogor."
    ),
    (
        "IHSG berhasil menguat berkat dukungan penguatan harga komoditas batu bara dan minyak sawit yang mendorong sentimen positif terhadap emiten sektor energi dan agribisnis.",
        "Saham seperti ITMG, ADMR, dan AALI mencatat kenaikan signifikan seiring optimisme investor terhadap kenaikan permintaan global pasca pembukaan kembali aktivitas ekonomi di Tiongkok.",
        "Siswa SD merayakan Hari Guru Nasional dengan upacara dan pemberian bunga kepada guru di sekolah mereka."
    ),
    (
        "IHSG melemah terbatas pada sesi perdagangan siang hari karena aksi profit taking setelah penguatan signifikan selama tiga hari berturut-turut.",
        "Analis teknikal menyebutkan bahwa indeks sedang mengalami koreksi sehat dan peluang rebound tetap terbuka jika support psikologis tidak ditembus.",
        "Kegiatan donor darah massal dilakukan oleh pegawai BUMN bekerja sama dengan Palang Merah Indonesia."
    ),
    (
        "IHSG tertekan oleh kekhawatiran investor terhadap pemburukan hubungan diplomatik antara Indonesia dan mitra dagang utama di kawasan Asia Timur.",
        "Gejolak geopolitik yang meningkat dianggap berpotensi mengganggu jalur pasokan ekspor dan menurunkan kinerja emiten manufaktur dan pertanian.",
        "Lomba mural bertema lingkungan hidup diikuti oleh 50 peserta dari berbagai komunitas seni jalanan di Yogyakarta."
    ),
    (
        "IHSG ditutup menguat menjelang akhir bulan setelah investor mengantisipasi window dressing oleh manajer investasi besar yang berupaya memperbaiki kinerja portofolio mereka.",
        "Fenomena window dressing ini kerap terjadi pada akhir kuartal dan akhir tahun, mendorong pembelian saham-saham berkapitalisasi besar.",
        "Para pelajar SMA mengikuti simulasi sidang PBB sebagai bagian dari program penguatan diplomasi muda di Jakarta Selatan."
    ),
    (
        "IHSG menguat berkat sentimen positif dari pengumuman kinerja emiten kuartal III yang secara umum menunjukkan pertumbuhan laba bersih yang solid di sektor perbankan dan konsumer.",
        "Saham-saham blue chip seperti BBRI, ICBP, dan UNVR menjadi incaran investor institusi karena stabilitas pendapatan dan prospek jangka panjangnya.",
        "Perkumpulan pengusaha muda menggelar bazar UMKM di taman kota untuk mempromosikan produk lokal kepada masyarakat umum."
    ),
    (
        "IHSG bergerak stagnan meski indeks manufaktur menunjukkan kenaikan, karena investor menilai adanya ketimpangan antara peningkatan produksi dan permintaan riil domestik.",
        "Data makroekonomi positif tidak selalu serta-merta direspons oleh penguatan indeks karena pelaku pasar mempertimbangkan banyak variabel lain.",
        "Petugas damkar menyelamatkan seekor kucing yang terjebak di atap rumah warga di kawasan Bekasi Timur."
    ),
    (
        "IHSG sempat menguat sebelum akhirnya ditutup melemah karena koreksi pada sektor teknologi dan transportasi yang menjadi target profit taking menjelang akhir pekan.",
        "Aksi ambil untung ini dinilai wajar oleh analis teknikal karena indeks telah menguat cukup signifikan dalam jangka pendek.",
        "Komunitas pecinta tanaman hias mengadakan workshop perawatan anggrek bulan dan kaktus di Balai Flora Jakarta."
    ),
    (
        "IHSG ditutup menguat 0,82% ke level 6.950 setelah Bank Indonesia mengumumkan tetap mempertahankan suku bunga acuan di level 6,25%, sesuai ekspektasi pasar.",
        "Keputusan BI ini memberi sinyal stabilitas moneter yang disambut positif oleh investor, terutama di sektor properti dan perbankan.",
        "Kompetisi film dokumenter pelajar diadakan oleh komunitas perfilman lokal dengan tema keragaman budaya nusantara."
    ),
    (
        "IHSG masih berada dalam tren turun jangka pendek karena kekhawatiran akan potensi perlambatan ekonomi Tiongkok yang berdampak pada ekspor Indonesia.",
        "Saham-saham berbasis komoditas seperti ANTM, INCO, dan TINS mengalami tekanan jual karena sentimen negatif dari penurunan permintaan global.",
        "Museum maritim di Surabaya mengadakan pameran kapal tradisional dan sejarah pelayaran nusantara."
    ),
    (
        "IHSG berhasil rebound setelah rilis data neraca perdagangan yang mencatat surplus lebih tinggi dari perkiraan konsensus analis.",
        "Data ekspor yang membaik berkontribusi pada penguatan saham emiten pelayaran, logistik, dan komoditas ekspor utama.",
        "Festival musik jazz bertaraf internasional kembali digelar di kawasan Ancol dengan menghadirkan musisi dari lima negara."
    ),
    (
        "IHSG masih dibayangi tekanan eksternal dari kebijakan The Fed yang diperkirakan masih hawkish hingga akhir tahun.",
        "Imbas dari outlook suku bunga tinggi membuat saham-saham sektor teknologi dan startup digital mengalami koreksi lanjutan.",
        "Sekolah menengah atas di Papua memenangkan lomba riset ilmiah nasional tingkat pelajar dalam bidang bioteknologi."
    ),
    (
        "Pergerakan IHSG hari ini didorong oleh sentimen positif dari stabilnya harga minyak dunia dan penguatan pasar saham regional Asia.",
        "Saham sektor energi dan petrokimia menjadi penopang utama indeks setelah harga minyak mentah global menunjukkan tren stabil di atas USD 80 per barel.",
        "Pameran edukasi pertanian digelar di Jember untuk memperkenalkan teknologi pertanian presisi kepada petani lokal."
    ),
    (
        "IHSG sempat tertekan karena kekhawatiran pasar terhadap implementasi pajak karbon yang dapat membebani kinerja perusahaan sektor energi dan manufaktur.",
        "Pelaku pasar masih mencermati bagaimana kebijakan transisi energi akan berdampak terhadap bottom line emiten-emiten besar.",
        "Pemerintah daerah meluncurkan program penanggulangan banjir berbasis komunitas di kawasan rawan genangan air."
    ),
    (
        "IHSG stagnan pada awal perdagangan pekan ini karena pelaku pasar menunggu kepastian arah kebijakan fiskal dalam RAPBN tahun depan.",
        "Investor cenderung wait and see terhadap sektor konstruksi dan BUMN karya yang sangat bergantung pada alokasi anggaran infrastruktur.",
        "Lomba robotik pelajar tingkat nasional sukses digelar dengan partisipasi dari 20 provinsi di Indonesia."
    ),
    (
        "IHSG dibuka menguat setelah investor merespon positif terhadap sinyal pemulihan ekonomi domestik pasca data penjualan ritel menunjukkan pertumbuhan tahunan sebesar 5,2%.",
        "Kenaikan konsumsi masyarakat menjadi katalis bagi sektor konsumer dan ritel yang mendorong indeks ke zona hijau.",
        "Klub pecinta astronomi mengadakan pelatihan astrofotografi menggunakan kamera DSLR di area terbuka hijau kota."
    ),
    (
        "IHSG kembali menguji resistance psikologis di level 7.000 setelah seminggu penuh mengalami akumulasi oleh investor institusi lokal.",
        "Volume transaksi meningkat tajam di saham-saham lapis satu seperti BBCA, TLKM, dan ASII, menandakan potensi breakout jangka pendek.",
        "Komunitas pemuda desa meluncurkan program bank sampah digital untuk meningkatkan kesadaran lingkungan."
    ),
    (
        "IHSG melemah terbatas di tengah kekhawatiran atas potensi resesi di kawasan Eropa yang bisa berdampak pada permintaan global dan ekspor Indonesia.",
        "Beberapa sektor seperti otomotif dan industri dasar mengalami tekanan karena kekhawatiran penurunan permintaan ekspor ke zona euro.",
        "Festival makanan khas nusantara digelar selama tiga hari di alun-alun kota untuk mendukung UMKM lokal."
    ),
    (
        "IHSG ditutup menguat tipis pada sesi akhir pekan seiring aksi beli selektif investor domestik terhadap saham-saham blue chip seperti BBCA dan UNVR.",
        "Aksi akumulasi tersebut terjadi setelah adanya rilis data ekonomi domestik yang menunjukkan pertumbuhan PDB kuartal II lebih baik dari perkiraan.",
        "Para siswa SMK mengikuti pelatihan penggunaan perangkat lunak desain grafis di Balai Latihan Kerja kota."
    ),
    (
        "IHSG terkoreksi 0,73% akibat kekhawatiran pelaku pasar terhadap inflasi global dan efek domino dari tingginya harga pangan dunia.",
        "Sektor konsumer dan logistik mengalami tekanan karena investor memperkirakan kenaikan biaya operasional dan penurunan daya beli masyarakat.",
        "Komunitas sepeda melakukan kegiatan touring sejauh 80 km dari Semarang ke Yogyakarta dalam rangka kampanye hidup sehat."
    ),
    (
        "IHSG menguat di tengah penguatan mata uang rupiah terhadap dolar AS, memberi kelegaan pada emiten dengan beban utang luar negeri besar.",
        "Saham seperti GJTL, PPRO, dan AKRA mencatat kenaikan signifikan karena sensitivitas tinggi terhadap fluktuasi nilai tukar.",
        "Festival film pendek bertema lingkungan hidup diselenggarakan di kampus Universitas Negeri Surabaya."
    ),
    (
        "IHSG bergerak di zona merah setelah rilis data cadangan devisa menunjukkan penurunan akibat intervensi BI untuk menstabilkan kurs rupiah.",
        "Penurunan ini memicu kekhawatiran pasar terkait ketahanan eksternal dan menekan sektor perbankan dan telekomunikasi.",
        "Anak-anak sekolah dasar mengikuti lomba mewarnai di pusat perbelanjaan dalam rangka Hari Anak Nasional."
    ),
    (
        "IHSG menunjukkan volatilitas tinggi sepanjang hari perdagangan menyusul ketidakpastian global akibat ketegangan geopolitik di Timur Tengah.",
        "Investor memilih sektor-sektor defensif seperti utilitas dan barang konsumsi primer sebagai tempat berlindung dari fluktuasi pasar.",
        "Pemerintah kabupaten meluncurkan aplikasi layanan publik terintegrasi berbasis Android di acara HUT kabupaten."
    ),
    (
        "IHSG bergerak mendatar karena minimnya katalis positif baik dari dalam negeri maupun dari bursa global.",
        "Saham-saham lapis dua menjadi incaran pelaku pasar harian yang mencari potensi teknikal rebound dalam jangka pendek.",
        "Panitia lomba balap perahu tradisional mengumumkan pembatalan acara karena faktor cuaca ekstrem di kawasan pesisir."
    ),
    (
        "IHSG menguat setelah investor merespon positif terhadap pidato Menteri Keuangan yang menyatakan bahwa defisit APBN berada di bawah target.",
        "Sinyal fiskal positif ini mendorong penguatan saham sektor konstruksi dan perbankan syariah yang sensitif terhadap stimulus fiskal.",
        "Para pengrajin batik mengikuti pameran internasional di Malaysia dengan dukungan pemerintah daerah."
    ),
    (
        "IHSG ditutup melemah seiring dengan turunnya harga komoditas global seperti batu bara dan CPO yang menjadi andalan ekspor Indonesia.",
        "Saham-saham sektor energi dan agribisnis seperti PTBA, ADRO, dan AALI terkoreksi cukup dalam akibat sentimen negatif tersebut.",
        "Lomba pidato antar mahasiswa jurusan hukum membahas tema 'Etika dan Demokrasi dalam Era Digital'."
    ),
    (
        "IHSG dibuka stagnan meskipun data penjualan otomotif menunjukkan tren pemulihan berkelanjutan dalam tiga bulan terakhir.",
        "Investor masih menunggu rilis suku bunga acuan sebelum mengambil posisi besar di sektor manufaktur dan industri berat.",
        "Pusat bahasa daerah meluncurkan kamus daring interaktif untuk mendokumentasikan bahasa lokal yang hampir punah."
    ),
    (
        "IHSG mencoba menembus resistance teknikal di 7.050 namun gagal akibat tekanan jual dari investor asing yang mencatat net sell harian.",
        "Penurunan ini diiringi dengan melemahnya indeks regional Asia yang mencerminkan risk-off sentiment di emerging markets.",
        "Lomba panjat pinang diadakan di lapangan kecamatan untuk memperingati Hari Kemerdekaan Republik Indonesia."
    ),
    (
        "IHSG ditutup turun 1,1% ke level 6.820 usai Bank Indonesia menaikkan suku bunga acuan sebesar 25 bps menjadi 6,5%.",
        "Kenaikan suku bunga biasanya menekan sektor properti dan konstruksi karena meningkatnya biaya pinjaman dan risiko pembiayaan.",
        "Festival kuliner khas pesisir digelar di alun-alun kota dengan menghadirkan 50 tenant UMKM makanan laut."
    ),
    (
        "IHSG rebound setelah net buy asing mencapai Rp450 miliar, terutama di saham-saham sektor perbankan dan energi.",
        "Arus masuk dana asing ini menjadi sinyal pemulihan kepercayaan investor global terhadap pasar saham domestik.",
        "Pameran kerajinan tangan oleh pelaku UMKM digelar di gedung serbaguna desa setiap akhir pekan."
    ),
    (
        "IHSG melemah setelah investor asing mencatatkan net sell selama lima hari berturut-turut, total Rp1,2 triliun.",
        "Pelemahan terutama terjadi di saham-saham indeks LQ45 dan IDX30 yang menjadi target utama pelepasan oleh investor asing.",
        "Kompetisi desain interior antar mahasiswa arsitektur diadakan di kampus teknik sipil ITB."
    ),
    (
        "IHSG stabil meskipun BI mempertahankan suku bunga acuan di level 6%, dengan pernyataan dovish terkait inflasi yang terkendali.",
        "Sektor konsumer dan ritel mendapat angin segar dari keputusan ini karena kemungkinan adanya pertumbuhan konsumsi rumah tangga.",
        "Pentas seni budaya Betawi dihadiri oleh ratusan warga dalam rangka Hari Ulang Tahun Jakarta."
    ),
    (
        "IHSG terkoreksi karena kekhawatiran akan potensi outflow dari investor asing usai The Fed memberikan sinyal hawkish lanjutan.",
        "Ketidakpastian global menyebabkan pelaku pasar melakukan risk-off dan menjual aset di pasar negara berkembang seperti Indonesia.",
        "Pelatihan dasar pemrograman Python diberikan gratis oleh komunitas open source di perpustakaan kota."
    ),
    (
        "IHSG menguat 0,94% ke level 7.010 setelah BI mengumumkan stabilitas sektor perbankan tetap terjaga meskipun suku bunga tinggi.",
        "Kinerja bank-bank besar seperti BBRI dan BMRI mendukung penguatan indeks karena margin bunga bersih tetap solid.",
        "Lomba penulisan esai bertema literasi digital diselenggarakan oleh kementerian komunikasi dan informatika."
    ),
    (
        "IHSG kembali tertekan di bawah level psikologis 6.900 setelah IDX30 mencatatkan penurunan agregat sebesar 1,4% dalam seminggu.",
        "Saham-saham big cap yang tergabung dalam IDX30 menjadi penyumbang koreksi terbesar karena tekanan jual asing dan aksi ambil untung lokal.",
        "Pameran buku bekas terbesar di Jawa Tengah dibuka selama seminggu dengan diskon hingga 90%."
    ),
    (
        "IHSG menguat terbatas seiring dengan penguatan indeks IDX30 sebesar 0,5%, didorong oleh saham-saham sektor infrastruktur dan telekomunikasi.",
        "Penguatan IDX30 seringkali menjadi acuan kekuatan IHSG secara menyeluruh karena proporsi kapitalisasi pasarnya yang besar.",
        "Kegiatan penghijauan sekolah dengan penanaman 500 pohon dilakukan oleh siswa dan guru di area lingkungan sekolah."
    ),
    (
        "IHSG masih sideways karena pelaku pasar menantikan keputusan BI meeting berikutnya yang diperkirakan akan mempertahankan suku bunga.",
        "Ketidakpastian arah suku bunga membuat investor mengalihkan sementara portofolio ke obligasi negara sebagai bentuk lindung nilai.",
        "Lomba fotografi alam terbuka menarik ratusan peserta dari komunitas pecinta alam dan fotografer amatir."
    ),
    (
        "IHSG mencatat net foreign outflow terbesar dalam tiga bulan terakhir, mencapai Rp2,3 triliun, memicu aksi jual panik di pasar.",
        "Investor asing melepas saham sektor keuangan dan consumer goods setelah sentimen negatif dari outlook inflasi global.",
        "Gerakan donasi buku untuk daerah terpencil berhasil mengumpulkan lebih dari 5.000 eksemplar dari masyarakat."
    ),
    (
        "IHSG menguat tipis ke 6.935 ditopang sentimen positif dari surplus neraca perdagangan Indonesia sebesar USD 3,5 miliar.",
        "Surplus perdagangan memberi ruang bagi penguatan rupiah dan memperkuat keyakinan investor terhadap stabilitas ekonomi domestik.",
        "Festival seni lukis jalanan diadakan di trotoar Malioboro dengan peserta dari berbagai daerah."
    ),
    (
        "IHSG melemah 0,8% setelah imbal hasil obligasi AS tenor 10 tahun kembali naik ke atas 4,3%, memicu aksi jual di pasar saham regional.",
        "Kenaikan yield obligasi AS membuat aset berisiko seperti saham Indonesia kurang menarik bagi investor global.",
        "Turnamen e-sport lokal Mobile Legends diikuti oleh lebih dari 300 peserta dari kalangan pelajar."
    ),
    (
        "IHSG berhasil menutup gap teknikal pada level 6.890 setelah koreksi tajam pekan lalu, membuka peluang bullish reversal jangka pendek.",
        "Analis teknikal melihat adanya pola morning star pada candle harian, mengindikasikan potensi pembalikan arah.",
        "Komunitas lari pagi mengadakan event 'City Run' keliling pusat kota dengan rute sepanjang 10 km."
    ),
    (
        "IHSG sideways sepanjang hari seiring volume perdagangan yang menipis karena pelaku pasar menunggu hasil FOMC meeting dini hari nanti.",
        "Situasi wait and see umum terjadi di pasar modal menjelang keputusan suku bunga dari The Fed yang bisa mempengaruhi aliran modal.",
        "Pameran otomotif tahunan menampilkan mobil listrik terbaru dari berbagai produsen dalam negeri dan luar negeri."
    ),
    (
        "IHSG ditutup menguat 1,2% setelah rilis data inflasi menunjukkan penurunan ke level 2,8% yoy, di bawah ekspektasi analis.",
        "Penurunan inflasi membuka peluang penurunan suku bunga BI di masa depan dan mendorong saham-saham sensitif suku bunga.",
        "Pelatihan digital marketing gratis diselenggarakan oleh komunitas pemuda kreatif di kantor kecamatan."
    ),
    (
        "IHSG terkoreksi setelah lonjakan harga minyak mentah dunia ke atas USD 90 per barel menimbulkan kekhawatiran akan tekanan inflasi.",
        "Saham sektor transportasi dan logistik terpukul akibat potensi kenaikan biaya operasional yang signifikan.",
        "Acara donor darah massal diadakan oleh organisasi mahasiswa kedokteran dalam rangka Hari Kesehatan Nasional."
    ),
    (
        "IHSG masih bergerak di area konsolidasi sempit antara 6.880 – 6.940 seiring minimnya katalis baru dari dalam dan luar negeri.",
        "Fase konsolidasi biasanya terjadi setelah pergerakan signifikan sebagai bentuk akumulasi atau distribusi pasar.",
        "Lomba cerdas cermat tingkat SMA se-kota diselenggarakan oleh Dinas Pendidikan di aula balai kota."
    ),
    (
        "IHSG naik signifikan setelah OJK mengumumkan relaksasi aturan IPO yang memudahkan startup masuk ke papan utama BEI.",
        "Saham teknologi dan e-commerce merespon positif karena regulasi ini memberi peluang ekspansi lebih cepat ke publik.",
        "Komunitas pecinta astronomi mengadakan pengamatan hujan meteor bersama di kawasan pegunungan Ungaran."
    ),
    (
        "IHSG menguat 0,7% berkat penguatan saham perbankan besar menyusul rilis kinerja keuangan Q2 yang mencatat pertumbuhan laba bersih dua digit.",
        "Investor optimis terhadap outlook sektor perbankan di tengah pertumbuhan kredit yang solid dan rasio NPL yang terjaga.",
        "Para siswa SMA mengikuti simulasi sidang PBB dalam acara Model United Nations tingkat regional."
    ),
    (
        "IHSG melemah di sesi kedua karena tekanan jual dari sektor energi menyusul kabar penurunan permintaan batubara dari China.",
        "Saham ADRO dan PTBA terkoreksi lebih dari 2% akibat sentimen negatif terhadap outlook ekspor komoditas.",
        "Turnamen catur antar RT diselenggarakan di balai RW dalam rangka memperingati Hari Kemerdekaan RI ke-80."
    ),
    (
        "IHSG melemah 0,6% ke level 6.875 dipicu oleh pelemahan rupiah terhadap dolar AS yang menembus Rp16.200 per USD.",
        "Pelemahan rupiah meningkatkan beban impor dan membuat investor asing cenderung menarik dana dari pasar domestik.",
        "Festival kopi nusantara berlangsung meriah di Lapangan Merdeka, diikuti oleh puluhan barista dari seluruh Indonesia."
    ),
    (
        "IHSG mencatat kenaikan harian tertinggi dalam dua bulan terakhir usai pemerintah mengumumkan insentif fiskal baru untuk sektor industri.",
        "Stimulus fiskal berperan penting dalam mendorong ekspansi perusahaan publik di sektor manufaktur dan transportasi.",
        "Siswa kelas 11 mengadakan kegiatan studi lapangan ke pabrik pengolahan air bersih sebagai bagian dari kurikulum IPA."
    ),
    (
        "IHSG ditutup menguat 1,05% setelah rilis data manufaktur PMI Indonesia menunjukkan ekspansi di zona 52,2 poin.",
        "Data PMI yang berada di atas 50 menandakan ekspansi sektor industri dan mendorong optimisme terhadap pertumbuhan ekonomi.",
        "Acara bazar buku murah digelar di taman kota dengan ribuan judul buku dari berbagai penerbit."
    ),
    (
        "IHSG bergerak variatif dipengaruhi ketidakpastian seputar debt ceiling di Amerika Serikat yang memicu volatilitas global.",
        "Sentimen global seperti risiko gagal bayar AS bisa menekan pasar negara berkembang termasuk Indonesia melalui arus modal keluar.",
        "Turnamen sepak bola antar kampung digelar setiap sore selama bulan Agustus dengan total hadiah jutaan rupiah."
    ),
    (
        "IHSG terkoreksi karena aksi profit taking menjelang pengumuman neraca transaksi berjalan kuartal kedua.",
        "Investor cenderung wait and see terhadap data CAD karena bisa mempengaruhi stabilitas eksternal dan nilai tukar rupiah.",
        "Para pelajar SMA mengikuti pelatihan penulisan berita yang diadakan oleh kantor berita lokal."
    ),
    (
        "IHSG rebound setelah Bank Indonesia mengumumkan akan melakukan intervensi di pasar valas untuk menstabilkan rupiah.",
        "Kebijakan intervensi BI ini disambut positif oleh pelaku pasar karena memberi kepastian terhadap fluktuasi mata uang.",
        "Lomba daur ulang sampah plastik menjadi karya seni diikuti oleh siswa SD dan SMP se-kecamatan."
    ),
    (
        "IHSG turun 0,9% menyusul laporan defisit neraca perdagangan akibat lonjakan impor migas dan penurunan ekspor nonmigas.",
        "Defisit perdagangan berdampak negatif terhadap sentimen pasar karena meningkatkan tekanan pada rupiah dan cadangan devisa.",
        "Komunitas pecinta hewan mengadakan vaksinasi rabies gratis di taman kota."
    ),
    (
        "IHSG mencatat penguatan moderat karena investor menyambut positif hasil rating Indonesia dari Fitch yang tetap pada BBB dengan outlook stabil.",
        "Rating kredit negara yang kuat meningkatkan kepercayaan investor institusi terhadap fundamental ekonomi Indonesia.",
        "Festival makanan tradisional khas Kalimantan digelar di aula universitas sebagai bagian dari program kebudayaan."
    ),
    (
        "IHSG konsolidasi di level 6.920-6.960 menunggu rilis data inflasi dan kebijakan subsidi energi dari pemerintah.",
        "Ketidakpastian subsidi BBM dan listrik berpotensi mempengaruhi margin emiten di sektor transportasi dan utilitas.",
        "Ratusan mahasiswa mengikuti seminar nasional tentang green technology dan energi baru terbarukan."
    ),
    (
        "IHSG menguat 0,7% setelah pelaku pasar menyerap positif sinyal dari pemerintah untuk mempercepat realisasi belanja APBN.",
        "Realisasi belanja pemerintah menjadi salah satu penggerak utama pertumbuhan PDB dan laba emiten sektor konstruksi dan infrastruktur.",
        "Acara lari maraton tahunan diselenggarakan di sepanjang jalan protokol ibu kota dan diikuti oleh ribuan peserta."
    ),
        (
        "IHSG ditutup melemah 0,75% ke level 6.850 karena investor mengantisipasi potensi kenaikan harga BBM subsidi dalam waktu dekat.",
        "Kekhawatiran atas inflasi akibat penyesuaian harga BBM dapat mengurangi daya beli masyarakat dan berdampak pada sektor konsumsi.",
        "Kompetisi fotografi lanskap diadakan di kawasan wisata pantai selatan dengan juri profesional."
    ),
    (
        "IHSG menguat setelah rilis laporan keuangan bank-bank besar menunjukkan lonjakan laba bersih kuartal kedua tahun ini.",
        "Pertumbuhan laba bersih yang kuat dari sektor perbankan menjadi katalis positif utama bagi penguatan indeks.",
        "Pentas seni budaya lokal digelar di pendopo kecamatan untuk memperingati hari jadi kota."
    ),
    (
        "IHSG bergerak di zona merah setelah kekhawatiran terhadap potensi perlambatan ekonomi Tiongkok mencuat kembali.",
        "Sebagai mitra dagang utama, kondisi ekonomi Tiongkok mempengaruhi permintaan ekspor Indonesia, khususnya komoditas.",
        "Mahasiswa jurusan teknik mengikuti pelatihan penggunaan printer 3D untuk prototyping alat industri."
    ),
    (
        "IHSG naik tipis di tengah mixed sentiment global, dengan investor mencerna hasil pertemuan G20 terkait ketegangan geopolitik.",
        "Sentimen global bisa menjadi pemicu volatilitas jangka pendek meski fundamental domestik tetap kuat.",
        "Pameran lukisan kontemporer diselenggarakan oleh komunitas seniman muda di gedung kesenian daerah."
    ),
    (
        "IHSG ditutup menguat 1,3% berkat masuknya capital inflow asing senilai Rp2,1 triliun ke saham-saham bluechip.",
        "Masuknya dana asing menunjukkan meningkatnya kepercayaan terhadap prospek ekonomi Indonesia jangka menengah.",
        "Festival film pelajar tingkat nasional menampilkan karya-karya dokumenter bertema sosial dan lingkungan."
    ),
    (
        "IHSG terkoreksi akibat kekhawatiran atas potensi kenaikan tarif cukai hasil tembakau yang berdampak pada emiten rokok.",
        "Sektor consumer cyclical seperti rokok sangat sensitif terhadap regulasi fiskal yang memengaruhi struktur harga produk.",
        "Lomba debat antar universitas berlangsung selama tiga hari di aula utama kampus teknik."
    ),
    (
        "IHSG stabil setelah Bank Indonesia mempertahankan suku bunga acuan di 6,00% dalam Rapat Dewan Gubernur bulan ini.",
        "Kebijakan suku bunga yang stabil menunjukkan konsistensi BI dalam menjaga keseimbangan antara pertumbuhan dan inflasi.",
        "Acara penanaman pohon bersama siswa SMA dan warga desa dilakukan untuk memperingati Hari Lingkungan Hidup."
    ),
    (
        "IHSG mengalami tekanan jual setelah investor merespons negatif outlook pertumbuhan ekonomi dunia versi IMF yang direvisi turun.",
        "Revisi pertumbuhan global menjadi sentimen negatif karena menandakan potensi perlambatan permintaan ekspor Indonesia.",
        "Komunitas otomotif menggelar gathering akbar dengan konvoi kendaraan antik sepanjang 20 km."
    ),
    (
        "IHSG menguat setelah pemerintah melaporkan realisasi penerimaan pajak melebihi target semester pertama tahun ini.",
        "Realisasi pajak yang baik memperkuat optimisme fiskal dan mendukung stabilitas makroekonomi nasional.",
        "Kompetisi coding online diselenggarakan untuk pelajar dan mahasiswa tingkat nasional dengan hadiah beasiswa."
    ),
    (
        "IHSG sempat terkoreksi tajam di sesi pagi sebelum akhirnya rebound setelah rilis data cadangan devisa yang tetap kuat di atas USD 136 miliar.",
        "Cadangan devisa yang besar memberikan kepercayaan terhadap kemampuan BI dalam menstabilkan nilai tukar rupiah.",
        "Pertunjukan wayang kulit semalam suntuk diadakan di lapangan desa dalam rangka sedekah bumi."
    ),

    (
        "IHSG ditutup melemah tipis 0,15% di tengah tekanan jual pada saham-saham sektor energi, menyusul penurunan harga batu bara global ke level terendah dalam 7 bulan terakhir.",
        "Penurunan harga batu bara memberikan tekanan pada saham emiten tambang seperti ADRO, PTBA, dan ITMG yang selama ini menjadi motor utama indeks.",
        "Komunitas pecinta astronomi menggelar malam pengamatan bintang di kawasan dataran tinggi Dieng."
    ),
    (
        "IHSG mampu membalikkan pelemahan dan ditutup menguat 0,5% setelah penguatan sektor perbankan merespons baik keputusan OJK yang melonggarkan aturan CKPN.",
        "Kebijakan pelonggaran CKPN mendorong optimisme akan pertumbuhan kredit dan penurunan beban provisi bank-bank besar.",
        "Lomba panjat pinang dalam rangka HUT RI ke-79 berlangsung meriah di lapangan kelurahan."
    ),
    (
        "IHSG terkoreksi 0,8% setelah investor merespons negatif outlook kenaikan suku bunga The Fed yang lebih lama dari perkiraan sebelumnya.",
        "Ekspektasi kenaikan suku bunga global dapat memicu arus keluar modal asing dari pasar saham domestik menuju aset safe haven.",
        "Pelatihan pembuatan kompos dari sampah rumah tangga diikuti oleh ibu-ibu PKK di kelurahan Mekarsari."
    ),
    (
        "IHSG menguat seiring sentimen positif dari rencana penurunan pajak dividen bagi investor domestik yang disampaikan dalam RAPBN 2026.",
        "Kebijakan ini diharapkan mampu meningkatkan partisipasi investor ritel lokal di pasar modal dan mendorong pendalaman pasar.",
        "Pertandingan ekshibisi bola voli antara alumni dan siswa SMA berlangsung seru dan penuh semangat."
    ),
    (
        "IHSG sempat bergerak fluktuatif setelah rilis inflasi tahunan yang sedikit di atas konsensus analis, mencapai 3,21% yoy.",
        "Inflasi yang lebih tinggi dari perkiraan dapat menurunkan daya beli dan memicu kekhawatiran akan potensi kenaikan suku bunga BI.",
        "Festival budaya Betawi digelar di Taman Mini Indonesia Indah dengan pertunjukan tanjidor dan lenong."
    ),
    (
        "IHSG ditutup menguat 1,1% dipimpin oleh sektor properti dan konstruksi setelah Kementerian PUPR merilis rencana percepatan proyek IKN tahap dua.",
        "Katalis dari proyek IKN mendorong aksi beli di saham-saham emiten konstruksi negara seperti PTPP, WIKA, dan ADHI.",
        "Lomba mewarnai anak-anak PAUD dan TK diadakan di pusat perbelanjaan sebagai bagian dari kampanye edukasi warna-warni ceria."
    ),
    (
        "IHSG stagnan di level 6.950 akibat minimnya sentimen baru menjelang libur panjang Idul Adha dan sepinya volume perdagangan.",
        "Hari libur panjang seringkali menyebabkan investor wait-and-see dan menghindari risiko short-term.",
        "Program vaksinasi rabies gratis bagi hewan peliharaan digelar oleh dinas peternakan kota."
    ),
    (
        "IHSG ditutup melemah setelah sentimen negatif datang dari outlook pertumbuhan ekonomi global oleh World Bank yang memangkas proyeksi untuk kawasan Asia Timur dan Pasifik.",
        "Outlook pertumbuhan yang melambat meningkatkan risiko terhadap ekspor Indonesia, khususnya sektor pertambangan dan agrikultur.",
        "Lomba kreasi makanan sehat antar sekolah dasar menarik perhatian para orang tua dan guru."
    ),
    (
        "IHSG naik 0,4% setelah BI merilis data penyaluran kredit sektor produktif yang meningkat signifikan sepanjang semester pertama.",
        "Pertumbuhan kredit produktif mencerminkan ekspansi bisnis dan mendukung target pertumbuhan ekonomi nasional.",
        "Pagelaran tari saman oleh mahasiswa Aceh menjadi puncak acara Festival Budaya Nusantara di kampus."
    ),
    (
        "IHSG berada di zona hijau setelah rilis laporan ketenagakerjaan yang menunjukkan penurunan tingkat pengangguran nasional menjadi 5,2%.",
        "Penurunan tingkat pengangguran menjadi sinyal positif bagi daya beli masyarakat dan konsumsi domestik.",
        "Pameran seni rupa mahasiswa ISI dibuka secara resmi oleh rektor dan menampilkan lukisan kontemporer serta instalasi multimedia."
    ),
        (
        "IHSG menguat 0,9% ditopang oleh rebound saham-saham teknologi setelah sentimen positif dari Nasdaq dan rilis data pertumbuhan e-commerce di Indonesia.",
        "Performa sektor teknologi menjadi penggerak utama IHSG, didorong oleh data konsumsi digital yang menunjukkan pertumbuhan dua digit tahunan.",
        "Kompetisi catur terbuka se-Jawa Tengah digelar di aula perpustakaan daerah dengan peserta lebih dari 300 orang."
    ),
    (
        "IHSG tertekan oleh aksi profit taking investor asing pasca penguatan tajam dalam tiga hari berturut-turut.",
        "Aksi ambil untung merupakan respons wajar atas rally teknikal dan tidak selalu mencerminkan perubahan tren fundamental.",
        "Seminar parenting diadakan oleh komunitas ibu muda dengan tema manajemen emosi anak usia dini."
    ),
    (
        "IHSG sempat anjlok di sesi pertama perdagangan setelah data neraca perdagangan menunjukkan surplus yang menyempit dibandingkan bulan sebelumnya.",
        "Penyempitan surplus perdagangan menimbulkan kekhawatiran terhadap ketahanan ekspor Indonesia di tengah ketidakpastian global.",
        "Komunitas trail run mengadakan lari lintas alam sejauh 12 km di lereng Gunung Ungaran."
    ),
    (
        "IHSG melanjutkan tren penguatan ditopang oleh saham-saham defensif seperti sektor konsumer dan telekomunikasi.",
        "Saham defensif menjadi pilihan utama investor saat terjadi ketidakpastian makro karena ketahanannya terhadap siklus ekonomi.",
        "Acara donor darah massal dilaksanakan di kantor kecamatan bekerja sama dengan PMI cabang Semarang."
    ),
    (
        "IHSG turun tipis 0,3% di tengah pelemahan mata uang rupiah terhadap dolar AS hingga menembus Rp15.800 per USD.",
        "Pelemahan rupiah dapat meningkatkan beban utang luar negeri korporasi dan memicu kekhawatiran inflasi impor.",
        "Kompetisi esai pelajar SMA tingkat nasional dengan tema 'Pemuda dan Inovasi Digital' diikuti lebih dari 1000 peserta."
    ),
    (
        "IHSG stagnan menjelang pidato kenegaraan presiden yang diperkirakan akan memuat arah kebijakan fiskal tahun depan.",
        "Pasar sering wait and see sebelum peristiwa makro penting seperti pidato kenegaraan atau pengumuman RAPBN.",
        "Lomba fotografi urban dilaksanakan di sekitar kawasan Kota Lama Semarang dengan tema arsitektur kolonial."
    ),
    (
        "IHSG melonjak 1,2% usai pemerintah mengumumkan stimulus fiskal tambahan untuk mendorong konsumsi domestik.",
        "Stimulus yang langsung menyasar sektor UMKM dan rumah tangga menimbulkan ekspektasi pertumbuhan ekonomi lebih cepat.",
        "Pentas drama musikal pelajar diselenggarakan sebagai bagian dari kegiatan ekstrakurikuler akhir tahun."
    ),
    (
        "IHSG bergerak mendatar meskipun mayoritas bursa regional Asia mengalami penguatan signifikan.",
        "Minimnya katalis domestik dan kekhawatiran atas perlambatan investasi menjadi faktor penghambat penguatan IHSG.",
        "Mahasiswa arsitektur mempresentasikan desain smart city di pameran kampus tahunan."
    ),
    (
        "IHSG terkoreksi di tengah kekhawatiran investor terhadap revisi proyeksi pertumbuhan ekonomi dari lembaga riset internasional.",
        "Revisi proyeksi pertumbuhan global seringkali memengaruhi outlook jangka pendek terhadap indeks pasar saham domestik.",
        "Turnamen e-sports Mobile Legends tingkat kabupaten diikuti oleh 24 tim dari berbagai sekolah."
    ),
    (
        "IHSG menguat setelah Gubernur BI menyatakan bahwa suku bunga tetap akan ditahan untuk mendukung stabilitas nilai tukar dan pertumbuhan.",
        "Kepastian arah suku bunga menjadi sinyal positif bagi pelaku pasar yang menghindari volatilitas kebijakan.",
        "Pelatihan menulis kreatif diikuti oleh siswa SMP dari berbagai daerah melalui platform daring."
    ),
        (
        "IHSG ditutup melemah 0,4% di tengah meningkatnya kekhawatiran pasar terhadap gejolak geopolitik di kawasan Timur Tengah yang berdampak pada harga minyak dunia.",
        "Lonjakan harga minyak dapat meningkatkan tekanan inflasi dan memperberat beban subsidi energi yang berdampak pada fiskal nasional.",
        "Lomba desain interior rumah minimalis diselenggarakan oleh fakultas teknik arsitektur kampus swasta di Bandung."
    ),
    (
        "IHSG menguat ke level 7.050 setelah rilis data cadangan devisa yang naik signifikan, mencerminkan stabilitas eksternal Indonesia di tengah ketidakpastian global.",
        "Peningkatan cadangan devisa memberikan ruang bagi Bank Indonesia untuk menjaga stabilitas rupiah dan likuiditas valas.",
        "Turnamen basket antar komunitas berlangsung meriah di GOR Saburai dengan diikuti oleh 16 tim dari berbagai kota."
    ),
    (
        "IHSG menguat setelah investor menyambut positif laporan laba kuartalan dari emiten perbankan besar seperti BBCA dan BBRI yang melampaui ekspektasi analis.",
        "Kinerja keuangan perbankan yang solid menjadi indikator pemulihan ekonomi nasional dan daya tahan sektor keuangan.",
        "Festival film pendek pelajar SMA menampilkan karya-karya bertema lingkungan hidup dan perubahan iklim."
    ),
    (
        "IHSG sempat mengalami tekanan jual menyusul rilis data inflasi AS yang lebih tinggi dari perkiraan, memicu kekhawatiran kenaikan suku bunga lebih agresif.",
        "Kenaikan inflasi global dapat mendorong capital outflow dari negara berkembang seperti Indonesia ke aset-aset dolar.",
        "Kompetisi debat bahasa Inggris antar SMA digelar secara daring dengan tema 'Teknologi dan Etika'."
    ),
    (
        "IHSG bergerak variatif setelah investor menanti kepastian terkait rencana merger antara dua emiten telekomunikasi besar di Indonesia.",
        "Kabar merger menciptakan spekulasi mengenai efisiensi industri dan potensi sinergi yang dapat menguntungkan investor.",
        "Komunitas fotografi lanskap mengadakan trip ke kawasan Bromo untuk pengambilan gambar matahari terbit."
    ),
    (
        "IHSG naik 0,7% usai pemerintah menyampaikan komitmen investasi asing senilai USD 3 miliar di sektor energi terbarukan.",
        "Masuknya investasi asing mencerminkan kepercayaan terhadap stabilitas iklim bisnis dan prospek pertumbuhan jangka panjang.",
        "Siswa kelas 6 SD memamerkan hasil proyek sains tentang daur ulang plastik di aula sekolah."
    ),
    (
        "IHSG terkoreksi ringan di tengah penantian pasar terhadap arah kebijakan fiskal yang akan diumumkan dalam Nota Keuangan RAPBN.",
        "Arah kebijakan fiskal sangat memengaruhi proyeksi pertumbuhan sektor-sektor strategis seperti infrastruktur dan kesehatan.",
        "Pentas musik akustik diselenggarakan oleh komunitas indie lokal di kafe sudut kota Yogyakarta."
    ),
    (
        "IHSG berada dalam tren konsolidasi setelah penguatan signifikan pekan sebelumnya, dengan volume perdagangan yang menurun drastis.",
        "Kondisi konsolidasi biasanya terjadi saat pasar mencari katalis baru dan pelaku pasar memilih sikap hati-hati.",
        "Workshop penulisan puisi digelar oleh Balai Bahasa untuk generasi muda di kawasan Nusa Tenggara Timur."
    ),
    (
        "IHSG menguat setelah Bank Indonesia menahan suku bunga acuan di level 6,25% dan menyampaikan pandangan optimis terhadap inflasi yang tetap terjaga.",
        "Stabilitas suku bunga menciptakan kepastian bagi pelaku usaha dan menjadi sinyal positif untuk pasar modal.",
        "Pelatihan budidaya hidroponik untuk ibu rumah tangga diadakan oleh dinas ketahanan pangan daerah."
    ),
    (
        "IHSG ditutup naik 0,6% dipimpin oleh saham emiten barang konsumsi, menyusul rilis data penjualan ritel yang meningkat 9,2% yoy.",
        "Kenaikan penjualan ritel mengindikasikan perbaikan daya beli masyarakat dan prospek pertumbuhan konsumsi domestik.",
        "Festival kuliner nusantara digelar di taman kota selama tiga hari dengan partisipasi UMKM kuliner lokal."
    ),
    (
        "IHSG menguat signifikan pada akhir perdagangan setelah pengumuman kerja sama strategis antara BUMN dan perusahaan energi global dalam proyek energi baru terbarukan.",
        "Investor merespons positif kolaborasi energi hijau karena dapat meningkatkan ekspektasi terhadap keberlanjutan ekonomi nasional dan nilai jangka panjang emiten terkait.",
        "Pentas seni tari daerah digelar di alun-alun kota dalam rangka memperingati Hari Tari Sedunia."
    ),
    (
        "IHSG tertekan akibat rilis data inflasi tahunan yang lebih tinggi dari ekspektasi, memicu kekhawatiran bahwa Bank Indonesia akan menaikkan suku bunga acuan dalam waktu dekat.",
        "Kenaikan inflasi dapat menurunkan daya beli masyarakat dan menyebabkan pengetatan kebijakan moneter yang berdampak negatif pada pasar modal.",
        "Komunitas penikmat kopi mengadakan festival biji kopi nusantara di Gedung Kesenian."
    ),
    (
        "IHSG ditutup melemah setelah rilis laporan keuangan emiten tambang menunjukkan penurunan laba bersih akibat penurunan harga komoditas global.",
        "Fluktuasi harga komoditas seperti batu bara dan nikel memiliki pengaruh besar terhadap kinerja emiten tambang di Bursa Efek Indonesia.",
        "Sekolah menengah kejuruan mengadakan pameran hasil karya teknologi siswa, termasuk robot sederhana dan alat pendeteksi banjir."
    ),
    (
        "IHSG mengalami tekanan jual setelah investor global menarik dana dari pasar negara berkembang akibat sinyal hawkish dari The Fed.",
        "Aksi capital outflow dari emerging markets seperti Indonesia menjadi reaksi umum terhadap ekspektasi kenaikan suku bunga AS.",
        "Kompetisi menggambar digital dengan tema budaya lokal diadakan oleh platform edukasi daring."
    ),
    (
        "IHSG stagnan di tengah minimnya sentimen domestik dan investor memilih wait and see menjelang laporan inflasi global dan data ketenagakerjaan AS.",
        "Periode minim katalis umumnya diikuti oleh rendahnya volatilitas dan volume transaksi harian yang menurun.",
        "Pentas monolog sastra oleh mahasiswa fakultas bahasa dan seni berlangsung khidmat dan penuh apresiasi."
    ),
    (
        "IHSG melanjutkan penguatannya untuk hari ketiga berturut-turut, ditopang oleh aksi beli investor institusi terhadap saham sektor finansial dan properti.",
        "Aksi akumulasi di saham sektor properti mencerminkan optimisme terhadap pulihnya permintaan perumahan dan proyek infrastruktur.",
        "Festival alat musik tradisional diikuti oleh berbagai sekolah dasar di kawasan perbatasan Kalimantan Barat."
    ),
    (
        "IHSG menguat setelah rilis data PMI manufaktur Indonesia menunjukkan ekspansi ke level tertinggi dalam enam bulan terakhir.",
        "PMI yang tinggi mencerminkan optimisme pelaku industri terhadap permintaan dan pertumbuhan produksi domestik.",
        "Pelatihan keterampilan digital untuk penyandang disabilitas dilaksanakan oleh lembaga swadaya masyarakat dengan dukungan CSR perusahaan teknologi."
    ),
    (
        "IHSG melemah akibat kekhawatiran pasar terhadap potensi resesi teknikal di Eropa dan penurunan permintaan ekspor dari negara tujuan utama Indonesia.",
        "Permintaan ekspor yang melambat dapat berdampak pada surplus perdagangan dan tekanan nilai tukar rupiah.",
        "Kegiatan bersih-bersih pantai bersama komunitas pecinta lingkungan diadakan di sepanjang garis pantai Parangtritis."
    ),
    (
        "IHSG rebound setelah pelemahan sebelumnya, didorong oleh kabar positif mengenai keberhasilan negosiasi ulang utang salah satu emiten besar di sektor infrastruktur.",
        "Restrukturisasi utang korporasi memberi sinyal perbaikan kondisi keuangan dan meningkatkan kepercayaan investor.",
        "Kompetisi robotik nasional untuk pelajar SMP menampilkan berbagai inovasi dalam bidang otomasi dan IoT."
    ),
    (
        "IHSG sempat mengalami volatilitas tinggi setelah pemerintah mengumumkan kebijakan baru terkait pembatasan ekspor mineral mentah.",
        "Kebijakan tersebut menciptakan ketidakpastian regulasi bagi emiten tambang dan memengaruhi proyeksi pendapatan jangka pendek.",
        "Lomba menulis cerpen digital untuk remaja digelar oleh perpustakaan nasional bekerja sama dengan platform literasi daring."
    ),
    (
        "IHSG bergerak menguat setelah Gubernur Bank Indonesia menyampaikan bahwa neraca transaksi berjalan Indonesia tetap terjaga di tengah fluktuasi global.",
        "Stabilitas transaksi berjalan mencerminkan fondasi ekonomi makro yang solid dan memperkuat keyakinan investor terhadap iklim investasi nasional.",
        "Festival budaya Betawi yang diadakan di Jakarta Selatan menampilkan pertunjukan lenong, tanjidor, dan kuliner khas."
    ),
    (
        "IHSG sempat terkoreksi karena aksi profit taking oleh investor ritel setelah reli empat hari berturut-turut mendorong indeks mendekati resistance teknikal.",
        "Profit taking wajar terjadi saat indeks menyentuh level teknikal tertentu dan belum ada katalis kuat lanjutan.",
        "Perlombaan perahu naga diadakan di danau buatan kawasan wisata Sumatera Utara untuk memperingati Hari Air Dunia."
    ),
    (
        "IHSG ditutup stagnan dengan sektor teknologi mencatatkan tekanan setelah rilis laporan pendapatan startup besar menunjukkan rugi kuartalan.",
        "Penurunan saham teknologi menandakan masih adanya tantangan monetisasi dan profitabilitas sektor digital di tengah kenaikan biaya operasional.",
        "Turnamen esports nasional kategori pelajar mempertemukan 32 tim dari seluruh Indonesia dalam babak penyisihan daring."
    ),
    (
        "IHSG menguat seiring penguatan nilai tukar rupiah yang menembus level psikologis Rp15.800 per USD setelah intervensi pasar valas oleh BI.",
        "Rupiah yang menguat cenderung berdampak positif bagi emiten yang memiliki beban impor tinggi dan utang valas.",
        "Komunitas seni mural lokal menggelar pameran seni jalanan dengan tema perubahan iklim di ruang terbuka publik."
    ),
    (
        "IHSG kembali ke zona hijau setelah penguatan saham sektor perbankan menyusul optimisme investor terhadap kenaikan kredit konsumsi menjelang akhir tahun.",
        "Pertumbuhan kredit konsumsi mencerminkan membaiknya kepercayaan masyarakat terhadap kondisi ekonomi.",
        "Pagelaran wayang kulit diadakan oleh karang taruna dalam rangka menyambut bulan purnama di desa budaya."
    ),
    (
        "IHSG mengalami volatilitas tinggi akibat laporan World Bank yang merevisi proyeksi pertumbuhan ekonomi Indonesia dari 5,3% menjadi 5,0%.",
        "Revisi turun proyeksi pertumbuhan ekonomi kerap membuat investor mengurangi eksposur terhadap saham-saham cyclical.",
        "Program vaksinasi massal terhadap hewan peliharaan diadakan oleh dinas peternakan di lapangan desa setiap akhir pekan."
    ),
    (
        "IHSG menguat setelah rilis indeks keyakinan konsumen menunjukkan peningkatan sentimen optimis terhadap kondisi ekonomi saat ini dan ekspektasi enam bulan ke depan.",
        "Peningkatan indeks kepercayaan konsumen sering menjadi indikator awal pemulihan konsumsi domestik.",
        "Acara pameran fotografi jurnalistik digelar oleh organisasi mahasiswa pers kampus dengan tema 'Realita dan Narasi'."
    ),
    (
        "IHSG menguat 1,1% setelah laporan Kementerian Keuangan menunjukkan surplus APBN berlanjut untuk bulan ketujuh berturut-turut.",
        "Surplus APBN mencerminkan efisiensi belanja negara dan potensi ruang fiskal untuk stimulus tambahan.",
        "Festival kopi nusantara kembali hadir di Bali dengan melibatkan lebih dari 50 pelaku UMKM dari berbagai provinsi."
    ),
    (
        "IHSG ditutup turun karena sentimen negatif dari penguatan dolar AS yang menekan nilai tukar rupiah serta menyebabkan kekhawatiran terhadap beban utang luar negeri korporasi.",
        "Kuatnya dolar AS dapat menekan likuiditas dan meningkatkan risiko pembiayaan ulang utang perusahaan Indonesia.",
        "Peluncuran aplikasi edukasi berbasis AR untuk anak usia dini dilakukan oleh startup lokal di bidang edtech."
    ),
    (
        "IHSG stagnan karena pelaku pasar menanti arah kebijakan subsidi energi dan harga BBM yang berdampak besar pada inflasi dan daya beli.",
        "Kebijakan BBM seringkali memiliki pengaruh langsung terhadap sektor transportasi, konsumer, dan emiten distribusi.",
        "Lokakarya kerajinan tangan anyaman bambu digelar oleh dinas pariwisata dan ekonomi kreatif provinsi."
    ),
    (
        "IHSG ditutup menguat tipis meskipun bursa global mengalami tekanan, menunjukkan adanya ketahanan domestik akibat aliran dana asing yang masih masuk ke saham big caps.",
        "Aliran dana asing ke saham berkapitalisasi besar memberi dukungan kuat terhadap pergerakan indeks meski kondisi eksternal tidak kondusif.",
        "Pelatihan pembuatan animasi dua dimensi untuk pelajar SMP diselenggarakan oleh komunitas kreatif lokal."
    ),
    (
        "IHSG bergerak fluktuatif karena pasar mencermati dampak potensi reshuffle kabinet terhadap keberlanjutan kebijakan fiskal dan ekonomi.",
        "Ketidakpastian politik domestik seperti perubahan menteri sering memicu sikap wait and see dari investor.",
        "Kegiatan menanam mangrove oleh relawan muda digelar di pesisir utara Pulau Jawa untuk mendukung program restorasi ekosistem."
    ),
    (
        "IHSG terkoreksi setelah laporan data perdagangan menunjukkan penurunan ekspor minyak sawit akibat hambatan logistik dan perubahan kebijakan impor negara tujuan.",
        "Ekspor komoditas unggulan yang melemah dapat menurunkan kinerja emiten sektor agrikultur dan perdagangan besar.",
        "Pentas tari modern oleh siswa SMA ditampilkan dalam rangkaian acara perpisahan sekolah."
    ),
    (
        "IHSG bergerak variatif menjelang penetapan suku bunga acuan oleh Bank Indonesia yang dinanti pelaku pasar untuk menilai arah kebijakan moneter ke depan.",
        "Keputusan BI rate menjadi salah satu katalis utama dalam menentukan arah pasar modal, terutama bagi sektor properti dan keuangan.",
        "Pameran teknologi inovatif untuk petani digelar di Yogyakarta dengan menampilkan traktor listrik dan irigasi pintar."
    ),
    (
        "IHSG naik tajam setelah pemerintah mengumumkan insentif pajak untuk sektor manufaktur dan ekspor yang dirancang untuk mendorong pemulihan industri.",
        "Kebijakan insentif fiskal dapat meningkatkan laba bersih emiten dan menciptakan daya tarik baru bagi investor institusional.",
        "Pentas musik akustik oleh mahasiswa seni dipadukan dengan pembacaan puisi bertema kemerdekaan."
    ),
    (
        "IHSG kembali ke zona merah setelah investor asing mencatatkan net sell sebesar Rp700 miliar akibat kekhawatiran resesi global yang meningkat.",
        "Net sell oleh investor asing menjadi indikator utama tekanan jual di pasar modal Indonesia.",
        "Turnamen futsal antar instansi pemerintah diselenggarakan untuk mempererat solidaritas ASN."
    ),
    (
        "IHSG ditutup menguat berkat kenaikan signifikan pada saham-saham perbankan setelah BI menyampaikan proyeksi pertumbuhan kredit yang positif untuk kuartal berikutnya.",
        "Ekspektasi pertumbuhan kredit yang tinggi menjadi katalis bagi saham bank besar seperti BBRI dan BBCA.",
        "Perpustakaan keliling berbasis sepeda motor menjangkau desa-desa terpencil di pegunungan Papua."
    ),
    (
        "IHSG stagnan akibat minimnya sentimen baru, dengan investor menunggu hasil FOMC meeting dan data inflasi AS sebagai acuan pergerakan global.",
        "Kondisi wait and see umum terjadi menjelang keputusan penting bank sentral global yang berdampak luas.",
        "Pembuatan film dokumenter oleh pelajar SMA tentang kehidupan nelayan di pesisir utara Jawa mendapat penghargaan lokal."
    ),
    (
        "IHSG menguat seiring dengan penguatan harga komoditas utama seperti batu bara dan CPO yang menjadi tulang punggung ekspor Indonesia.",
        "Harga komoditas global secara langsung memengaruhi emiten sektor energi dan agrikultur di BEI.",
        "Pagelaran wayang orang kolaboratif antar kampus diadakan sebagai bagian dari Pekan Budaya Nasional."
    ),
    (
        "IHSG dibuka menguat tipis namun berbalik arah setelah rilis neraca dagang mencatat defisit untuk pertama kalinya dalam 14 bulan.",
        "Defisit perdagangan bisa menekan nilai tukar rupiah dan menurunkan keyakinan pelaku pasar terhadap sektor ekspor.",
        "Lomba paduan suara tingkat SMA se-Jabodetabek diselenggarakan secara daring untuk menyambut Hari Musik Nasional."
    ),
    (
        "IHSG ditutup menguat setelah laporan keuangan kuartal II dari beberapa emiten besar menunjukkan pertumbuhan laba yang signifikan.",
        "Laporan keuangan yang solid biasanya menjadi pemicu rally jangka pendek di saham-saham terkait.",
        "Pameran buku murah diselenggarakan di pusat perbelanjaan untuk mendukung literasi masyarakat."
    ),
    (
        "IHSG terkoreksi tajam karena meningkatnya tensi geopolitik antara dua negara besar yang memengaruhi pasar global.",
        "Ketegangan geopolitik kerap membuat investor melakukan flight to safety dan menjual aset berisiko seperti saham.",
        "Festival kuliner nusantara digelar di alun-alun kota untuk mempromosikan UMKM makanan tradisional."
    ),
    (
        "IHSG bergerak datar menjelang libur panjang nasional, dengan volume perdagangan menurun drastis.",
        "Menjelang libur panjang, pelaku pasar cenderung wait and see dan melakukan posisi defensif.",
        "Komunitas sepeda gunung mengadakan kegiatan eksplorasi jalur baru di kaki Gunung Slamet."
    ),
    (
        "IHSG dibuka menguat berkat optimisme pasar terhadap rencana percepatan pembangunan Ibu Kota Nusantara yang diyakini akan mendorong sektor konstruksi.",
        "Percepatan pembangunan infrastruktur bisa menjadi katalis jangka panjang untuk saham konstruksi seperti WIKA dan PTPP.",
        "Lomba desain batik digital diikuti oleh ratusan peserta dari berbagai daerah di Indonesia."
    ),
    (
        "IHSG mencatatkan penguatan seiring penguatan bursa Asia yang merespons positif data inflasi China yang lebih rendah dari ekspektasi.",
        "Sentimen eksternal dari bursa regional dapat mempengaruhi arah indeks domestik secara intraday.",
        "Dinas kebudayaan menggelar pelatihan membatik untuk pelajar SMK sebagai bagian dari kurikulum budaya lokal."
    ),
    (
        "IHSG melemah karena aksi ambil untung investor setelah penguatan signifikan di sektor energi dalam seminggu terakhir.",
        "Profit taking adalah hal lumrah pasca penguatan tajam untuk menjaga kestabilan pasar.",
        "Acara donor darah massal diselenggarakan oleh organisasi kepemudaan di kampus teknik."
    ),
    (
        "IHSG menguat tipis setelah Bank Indonesia menyatakan akan tetap menjaga suku bunga acuan di level saat ini hingga akhir tahun.",
        "Kebijakan moneter yang akomodatif sering mendukung sentimen positif di pasar modal.",
        "Workshop pembuatan film pendek diikuti oleh siswa SMA dari lima provinsi sebagai bagian dari program nasional sinematografi pelajar."
    ),
    (
        "IHSG sempat melemah tetapi berhasil rebound jelang penutupan perdagangan karena penguatan saham blue chip seperti TLKM dan BBCA.",
        "Saham blue chip sering menjadi penopang indeks ketika saham lapis dua mengalami tekanan.",
        "Kegiatan lomba robotik pelajar diselenggarakan di universitas teknik ternama di Jakarta."
    ),
    (
        "IHSG mencatatkan net buy asing selama lima hari berturut-turut, menunjukkan kepercayaan investor global terhadap stabilitas ekonomi Indonesia.",
        "Aliran modal asing masuk ke pasar saham mencerminkan prospek ekonomi yang positif.",
        "Gerakan penanaman sejuta pohon dimulai dari sekolah dasar dan melibatkan komunitas lokal."
    ),
    (
        "IHSG menguat setelah IMF merilis laporan yang menyatakan bahwa Indonesia termasuk negara yang paling resilien di kawasan Asia Tenggara.",
        "Pujian dari lembaga internasional dapat memperkuat sentimen positif investor terhadap pasar domestik.",
        "Kompetisi debat Bahasa Inggris tingkat nasional diikuti oleh lebih dari 100 tim SMA."
    ),
    (
        "IHSG turun tipis karena rilis data inflasi nasional yang sedikit di atas ekspektasi, memicu kekhawatiran kenaikan suku bunga.",
        "Data inflasi yang tinggi berpotensi mengubah ekspektasi pasar terhadap kebijakan moneter.",
        "Festival film dokumenter digelar di kampus seni dan menyoroti isu-isu sosial lingkungan."
    ),
    (
        "IHSG dibuka stagnan meskipun harga minyak dunia melonjak, menunjukkan minimnya respons pasar terhadap sentimen global.",
        "Tidak semua sentimen global langsung direspons IHSG, tergantung relevansi sektoral.",
        "Pentas seni tradisional diadakan oleh siswa SMP dalam rangka menyambut Hari Kartini."
    ),
    (
        "IHSG terkoreksi setelah rilis data pengangguran menunjukkan kenaikan di bulan terakhir, menimbulkan kekhawatiran terhadap konsumsi domestik.",
        "Konsumsi domestik merupakan komponen penting dalam pertumbuhan ekonomi Indonesia.",
        "Pelatihan kerajinan tangan dari bahan daur ulang diselenggarakan oleh dinas sosial kota."
    ),
    (
        "IHSG menguat didorong oleh penguatan saham sektor consumer goods menjelang Ramadan, didorong oleh ekspektasi peningkatan konsumsi.",
        "Siklus musiman seperti Ramadan sering mempengaruhi saham sektor konsumer secara positif.",
        "Pameran seni rupa modern digelar di galeri nasional dengan tema urbanisasi dan identitas lokal."
    ),
    (
        "IHSG stagnan karena minimnya katalis baru dan investor menunggu hasil rapat dewan gubernur BI minggu depan.",
        "Pasar cenderung sideway saat tidak ada rilis data ekonomi penting atau katalis kuat.",
        "Bazar pakaian murah hasil produksi UMKM digelar oleh koperasi desa untuk menyambut tahun ajaran baru."
    ),
    (
        "IHSG ditutup naik 1,2% pada akhir perdagangan hari ini, didorong oleh lonjakan harga batu bara global yang mendorong saham-saham sektor energi.",
        "Penguatan harga komoditas dunia dapat memberi sentimen positif terhadap kinerja saham sektor terkait.",
        "Pelatihan jurnalistik dasar diberikan kepada siswa SMA sebagai bagian dari program literasi digital."
    ),
    (
        "IHSG terkoreksi setelah pemerintah mengumumkan kebijakan pengetatan impor barang konsumsi demi menjaga neraca perdagangan.",
        "Kebijakan fiskal dan perdagangan memiliki dampak signifikan terhadap sentimen pasar dan ekspektasi investor.",
        "Festival tari daerah diadakan oleh komunitas budaya di taman kota untuk memperingati hari jadi provinsi."
    ),
    (
        "IHSG bergerak fluktuatif seiring investor mencermati ketegangan politik regional yang memicu volatilitas pada pasar keuangan Asia.",
        "Situasi geopolitik di kawasan Asia mempengaruhi arus modal dan persepsi risiko investor global.",
        "Workshop penulisan kreatif diadakan secara daring oleh komunitas sastra kampus untuk umum."
    ),
    (
        "IHSG menguat setelah rilis data penjualan ritel nasional menunjukkan kenaikan yang lebih tinggi dari proyeksi analis.",
        "Data ekonomi yang menunjukkan pemulihan konsumsi domestik biasanya mendukung penguatan indeks.",
        "Lomba lukis mural bertema lingkungan hidup diselenggarakan oleh mahasiswa seni rupa."
    ),
    (
        "IHSG ditutup melemah meskipun bursa AS mencatatkan penguatan, menandakan adanya tekanan internal di pasar domestik.",
        "Tekanan internal seperti profit taking atau ketidakpastian kebijakan lokal bisa mengimbangi sentimen global yang positif.",
        "Komunitas penggiat fotografi alam menggelar pameran hasil ekspedisi ke taman nasional Indonesia."
    ),
    (
        "IHSG mencatatkan penguatan beruntun selama lima hari terakhir, ditopang oleh optimisme terhadap kinerja emiten kuartal tiga.",
        "Ekspektasi kinerja keuangan yang kuat dapat mendorong rally jangka pendek pada indeks saham.",
        "Program literasi keuangan untuk ibu rumah tangga diadakan oleh lembaga keuangan mikro setempat."
    ),
    (
        "IHSG melemah setelah nilai tukar rupiah terhadap dolar AS kembali menyentuh level psikologis Rp16.000 per dolar.",
        "Pelemahan nilai tukar rupiah dapat meningkatkan kekhawatiran pasar, khususnya pada sektor berbasis impor.",
        "Siswa SMK memamerkan produk inovasi teknologi hasil tugas akhir di acara Techno Fest 2025."
    ),
    (
        "IHSG bergerak sideways sepanjang hari perdagangan, mencerminkan keraguan pelaku pasar dalam menyikapi kondisi makroekonomi global.",
        "Ketidakpastian global dapat membuat pelaku pasar mengambil posisi netral dan menunggu kejelasan arah.",
        "Dinas pariwisata setempat mengadakan pelatihan pemandu wisata untuk mahasiswa jurusan perhotelan."
    ),
    (
        "IHSG menguat tipis setelah rilis laporan ekonomi tahunan Bank Indonesia yang menyoroti stabilitas moneter dan fiskal nasional.",
        "Laporan resmi dari lembaga keuangan negara bisa memperkuat persepsi positif investor terhadap prospek jangka menengah.",
        "Festival musik tradisional daerah diadakan di gedung kesenian oleh sanggar-sanggar lokal dari seluruh nusantara."
    ),
    (
        "IHSG terkoreksi karena kekhawatiran investor terhadap potensi lonjakan inflasi pasca kenaikan harga BBM subsidi.",
        "Kebijakan harga energi memiliki efek langsung terhadap ekspektasi inflasi dan daya beli masyarakat.",
        "Pameran pendidikan tinggi internasional diselenggarakan di Jakarta untuk memperkenalkan kampus luar negeri ke pelajar Indonesia."
    ),
    (
        "IHSG ditutup stagnan setelah investor menunggu hasil data pertumbuhan ekonomi kuartal terakhir yang akan dirilis pekan depan.",
        "Rilis data PDB menjadi salah satu indikator makroekonomi penting dalam menentukan arah pasar.",
        "Bazar pangan murah digelar oleh koperasi petani untuk membantu masyarakat menjelang hari besar keagamaan."
    ),
    (
        "IHSG mencatatkan net sell investor asing sebesar Rp1 triliun dalam satu hari, mengindikasikan capital outflow akibat ketidakpastian global.",
        "Capital outflow dalam jumlah besar dapat menimbulkan tekanan terhadap pasar modal domestik dan nilai tukar.",
        "Kegiatan belajar mengajar luar kelas diadakan oleh sekolah dasar dalam rangka mengenalkan siswa pada lingkungan sekitar."
    ),
    (
        "IHSG menguat berkat rencana pemerintah memberikan stimulus fiskal tambahan untuk mendorong pemulihan ekonomi pasca pandemi.",
        "Stimulus fiskal merupakan katalis positif yang sering meningkatkan sentimen investor terhadap emiten domestik.",
        "Seminar nasional tentang keamanan siber diadakan oleh fakultas teknik di sebuah universitas negeri."
    ),
    (
        "IHSG melemah meski harga minyak mentah dunia turun, menunjukkan bahwa sentimen domestik lebih dominan dibanding eksternal.",
        "Sentimen lokal seperti kebijakan pemerintah atau aksi korporasi dapat mengalahkan sentimen global sesekali.",
        "Kegiatan tanam pohon massal dilakukan oleh ribuan relawan di area bekas tambang yang direklamasi."
    ),
    (
        "IHSG kembali menembus level psikologis 7.000 didorong oleh lonjakan saham perbankan dan telekomunikasi.",
        "Level psikologis menjadi indikator penting dalam analisis teknikal dan psikologi pasar.",
        "Lomba karya tulis ilmiah tingkat nasional diikuti oleh mahasiswa dari berbagai perguruan tinggi Indonesia."
    )

]

# Convert to DataFrame
df = pd.DataFrame(triplets, columns=["anchor", "positive", "negative"])

# Save to CSV and JSON
csv_path = "datasets/news/trilpets/small/ihsg_triplets.csv"
json_path = "datasets/news/trilpets/small/ihsg_triplets.json"

df.to_csv(csv_path, index=False)
df.to_json(json_path, orient="records", lines=True)

csv_path, json_path
