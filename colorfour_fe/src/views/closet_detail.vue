<template>
  <div>
    <main>
      <div class="item-info-wrap">
        <button class="btn btn-outline-secondary edit-button" @click="editItem">復原單品</button>
        <button class="btn btn-outline-secondary" @click="deleteItem">永久刪除</button>
      </div>
      <section class="container">
        <div class="item-img">
          <img :src="item.image" alt="服飾圖片" />
        </div>
        <div class="item-info">
          <h1>{{ item.name }}</h1>
          <p>品牌: {{ item.brand }}</p>
          <p>價格: ${{ item.price }}</p>
          <p class="hashtag">種類：#{{ item.category }}</p>
          <p class="hashtag">標籤：{{ item.tags.map(tag => `#${tag}`).join(' ') }}</p>
          <p class="added-date">加入日期: {{ item.addedDate }}</p>
        </div>
      </section>
    </main>
  </div>
</template>


<script>
  import axios from "axios";

  export default {
  props: ['id'],
  data() {
    return {
      item: null, // 儲存對應id的項目
      items: [
        {
          id: 1,
          name: "白T萬歲",
          category: "t-shirt",
          brand: "UNIQLO",
          price: 150,
          addedDate: "2024/06/01",
          image: require("@/assets/img/Uniqlo_white_Tshirt.png"),
          tags: ["春天", "夏天", "休閒", "百搭"],
        },
        {
          id: 2,
          name: "連身裙",
          category: "dress",
          brand: "GU",
          price: 100,
          addedDate: "2024/06/02",
          image: require("@/assets/img/closet_02.png"),
          tags: ["春天", "夏天"],
        },
        {
          id: 3,
          name: "牛仔褲",
          category: "bottom",
          brand: "GU",
          price: 70,
          addedDate: "2024/06/03",
          image: require("@/assets/img/closet_03.png"),
          tags: ["春天", "夏天"],
        },
        {
          id: 4,
          name: "短褲",
          category: "bottom",
          brand: "UNIQLO",
          price: 220,
          addedDate: "2024/06/04",
          image: require("@/assets/img/closet_04.png"),
          tags: ["秋天", "冬天"],
        },
        {
          id: 5,
          name: "小白鞋",
          category: "shoes",
          brand: "無印",
          price: 80,
          addedDate: "2024/06/05",
          image: require("@/assets/img/closet_05.png"),
          tags: ["春天", "夏天"],
        },
        {
          id: 6,
          name: "西裝外套",
          category: "coat",
          brand: "GU",
          price: 120,
          addedDate: "2024/06/06",
          image: require("@/assets/img/closet_06.png"),
          tags: ["春天", "秋天"],
        },
        {
          id: 7,
          name: "墨鏡",
          category: "accessories",
          brand: "品牌C",
          price: 50,
          addedDate: "2024/06/07",
          image: "https://picsum.photos/300/200?random=6",
          tags: ["春天", "夏天"],
        },
        {
          id: 8,
          name: "手錶",
          category: "accessories",
          brand: "品牌A",
          price: 200,
          addedDate: "2024/06/08",
          image: "https://picsum.photos/300/200?random=7",
          tags: ["全年"],
        },
        {
          id: 9,
          name: "風衣",
          category: "coat",
          brand: "品牌B",
          price: 180,
          addedDate: "2024/06/09",
          image: "https://picsum.photos/300/200?random=8",
          tags: ["秋天", "冬天"],
        },
        {
          id: 10,
          name: "連帽衫",
          category: "top",
          brand: "品牌C",
          price: 130,
          addedDate: "2024/06/10",
          image: "https://picsum.photos/300/200?random=9",
          tags: ["秋天", "冬天"],
        },
        {
          id: 11,
          name: "T恤",
          category: "top",
          brand: "品牌E",
          price: 50,
          addedDate: "2024/06/11",
          image: "https://picsum.photos/300/200?random=12",
          tags: ["春天", "夏天"],
        },
        {
          id: 12,
          name: "針織衫",
          category: "top",
          brand: "GU",
          price: 90,
          addedDate: "2024/06/12",
          image: "https://picsum.photos/300/200?random=1",
          tags: ["秋天"],
        },
        {
          id: 13,
          name: "皮帶",
          category: "accessories",
          brand: "品牌F",
          price: 40,
          addedDate: "2024/06/13",
          image: "https://picsum.photos/300/200?random=13",
          tags: ["全年"],
        },
        {
          id: 14,
          name: "運動褲",
          category: "bottom",
          brand: "品牌G",
          price: 60,
          addedDate: "2024/06/14",
          image: "https://picsum.photos/300/200?random=14",
          tags: ["春天", "夏天"],
        },
        {
          id: 15,
          name: "棒球帽",
          category: "accessories",
          brand: "品牌H",
          price: 30,
          addedDate: "2024/06/15",
          image: "https://picsum.photos/300/200?random=15",
          tags: ["春天", "夏天"],
        },
        {
          id: 16,
          name: "羽絨服",
          category: "coat",
          brand: "品牌I",
          price: 250,
          addedDate: "2024/06/16",
          image: "https://picsum.photos/300/200?random=16",
          tags: ["冬天"],
        },
        {
          id: 17,
          name: "連身裙",
          category: "dress",
          brand: "品牌J",
          price: 110,
          addedDate: "2024/06/17",
          image: "https://picsum.photos/300/200?random=17",
          tags: ["春天", "夏天"],
        },
        {
          id: 18,
          name: "短靴",
          category: "shoes",
          brand: "品牌K",
          price: 140,
          addedDate: "2024/06/18",
          image: "https://picsum.photos/300/200?random=18",
          tags: ["秋天", "冬天"],
        },
        {
          id: 19,
          name: "牛仔外套",
          category: "coat",
          brand: "品牌L",
          price: 160,
          addedDate: "2024/06/19",
          image: "https://picsum.photos/300/200?random=19",
          tags: ["秋天", "冬天"],
        },
        {
          id: 20,
          name: "手提包",
          category: "accessories",
          brand: "品牌M",
          price: 90,
          addedDate: "2024/06/20",
          image: "https://picsum.photos/300/200?random=20",
          tags: ["全年"],
        },
      ],
    };
  },
  methods: {
  editItem() {
    // 恢復單品邏輯
    alert(`Restoring item: ${this.item.name}`);
    // 恢復成功後跳轉回 closet_trash.vue
    this.$router.push('/closet_trash');
  },
  deleteItem() {
    // 刪除單品邏輯
    alert(`Permanently deleting item: ${this.item.name}`);
    // 從列表中移除單品
    this.items = this.items.filter(item => item.id !== this.item.id);
    // 刪除成功後跳轉回 closet_trash.vue
    this.$router.push('/closet_trash');
  }
},
  created() {
  // Based on the props id, find the corresponding item
  console.log(this.id); // Check if the correct ID is being logged
  this.item = this.items.find((item) => item.id == this.id);
}
};
</script>

<style scoped>
  .bread {
    display: flex;
    margin: 0;
    padding: 0;
    list-style: none;
  }

  .bread li {
    padding: 0 20px;
  }

  .bread li + li {
    padding-left: 0;
  }

  .bread li + li:before {
    content: ">";
    color: #333;
    margin-right: 20px;
  }

  .bread a {
    text-decoration: none;
    color: #333;
  }

  main button {
    width: 15%;
    display: flex;
    align-items: end;
    justify-content: end;
  }

  .container {
    width: 90%;
    min-height: 400px;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    background-color: #ffffff;
    border: #333333 1px solid;
    box-shadow: #999999 3px 3px;
    margin: 0 auto;
    padding: 20px;
    border-radius: 20px;
    position: relative;
  }

  .item-info-wrap {
    width: 90%;
    display: flex;
    align-items: end;
    justify-content: end;
    margin-bottom: 20px;
  }

  .item-img {
    width: 45%;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .item-img img {
    width: 100%;
    height: 100%;
    border-radius: 20px;
    object-fit: cover;
  }

  .item-info {
    width: 50%;
    margin-left: 20px;
    display: flex;
    flex-direction: column;
    text-align: start;
    align-items: flex-start;
  }

  .item-info h1,
  .item-info p {
    margin: 5px 0;
  }

  .item-info h1 {
    font-size: 2rem;
    margin-bottom: 10px;
  }

  .item-info p {
    font-size: 1rem;
    margin-bottom: 10px;
  }

  .item-info .price {
    font-size: 1.5rem;
    color: #333;
  }

  .item-info .added-date {
    font-size: 1rem;
    color: #777;
  }

  @media screen and (max-width: 768px) {
    .item-img {
      width: 90%;
      margin-bottom: 20px;
    }

    .item-info {
      width: 90%;
      margin-left: 0;
    }

    main button {
      width: 30%;
    }
  }
</style>
