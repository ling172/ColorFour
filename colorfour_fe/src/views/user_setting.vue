<template>
  <div class="user-setting">
    <div class="account-management">
      <h3>登入帳戶管理</h3>
      <div class="linked-accounts">
        <div v-if="isGoogleLinked" class="account-item linked">
          <i class="fab fa-google"></i> Google 已連結
          <button @click="unlinkGoogle" class="unlink-button" :disabled="!canUnlinkGoogle">解除連結</button>
        </div>
        <div v-if="isLineLinked" class="account-item linked">
          <i class="fab fa-line"></i> Line 已連結
          <button @click="unlinkLine" class="unlink-button" :disabled="!canUnlinkLine">解除連結</button>
        </div>
        <div v-if="!isGoogleLinked" class="account-item" @click="connectGoogle">
          <i class="fab fa-google"></i> 連結 Google 帳號
        </div>
        <div v-if="!isLineLinked" class="account-item" @click="connectLine"><i class="fab fa-line"></i> 連結 Line 帳號</div>
      </div>
    </div>

    <div class="personal-info">
      <h3>編輯個人資料</h3>
      <div class="form-group">
        <label for="nickname">暱稱</label>
        <input type="text" id="nickname" v-model="nickname" placeholder="輸入暱稱" />
      </div>
      <div class="form-group">
        <label for="birthday">生日</label>
        <input type="date" id="birthday" v-model="birthday" />
      </div>
      <div class="form-group">
        <label for="email">Email</label>
        <input type="email" id="email" v-model="email" placeholder="輸入Email" />
      </div>
      <button @click="savePersonalInfo">保存</button>
    </div>
  </div>
</template>

<script>
  import { mapGetters, mapActions } from "vuex";

  export default {
    name: "user_setting",
    data() {
      return {
        nickname: "",
        birthday: "",
        email: "",
      };
    },
    computed: {
      ...mapGetters("auth", ["isAuthenticated", "user", "isGoogleLinked", "isLineLinked", "loginProvider"]),
      canUnlinkGoogle() {
        return this.isGoogleLinked && (this.loginProvider !== "google" || this.isLineLinked);
      },
      canUnlinkLine() {
        return this.isLineLinked && (this.loginProvider !== "line" || this.isGoogleLinked);
      },
    },
    methods: {
      ...mapActions("auth", ["fetchUserProfile", "updateUserProfile", "linkSocialAccount", "unlinkSocialAccount"]),
      async loadUserSettings() {
        console.log("載入設定中...");
        if (this.user) {
          this.nickname = this.user.nickname || "";
          this.birthday = this.user.birthday || "";
          this.email = this.user.email || "";
          console.log("設定載入完成:", {
            nickname: this.nickname,
            birthday: this.birthday,
            email: this.email,
            isGoogleLinked: this.isGoogleLinked,
            isLineLinked: this.isLineLinked,
            loginProvider: this.loginProvider,
          });
        } else {
          console.log("無法載入設定：使用者資料不存在");
        }
      },
      async savePersonalInfo() {
        console.log("開始儲存個人資料");
        try {
          await this.updateUserProfile({
            nickname: this.nickname,
            birthday: this.birthday,
            email: this.email,
          });
          console.log("個人資料儲存成功");
          alert("個人資料已成功更新");
        } catch (error) {
          console.error("儲存個人資料失敗:", error);
          alert("更新個人資料失敗，請稍後再試");
        }
      },
      async connectGoogle() {
        console.log("開始連結 Google 帳號");
        try {
          await this.linkSocialAccount("google");
          console.log("Google 帳號連結成功");
        } catch (error) {
          console.error("連結 Google 帳號失敗:", error);
          alert("連結 Google 帳號失敗，請稍後再試");
        }
      },
      async connectLine() {
        console.log("開始連結 Line 帳號");
        try {
          await this.linkSocialAccount("line");
          console.log("Line 帳號連結成功");
        } catch (error) {
          console.error("連結 Line 帳號失敗:", error);
          alert("連結 Line 帳號失敗，請稍後再試");
        }
      },
      async unlinkGoogle() {
        console.log("開始解除連結 Google 帳號");
        if (!this.canUnlinkGoogle) {
          alert("無法解除連結唯一的登入方式");
          return;
        }
        try {
          await this.unlinkSocialAccount("google");
          console.log("Google 帳號解除連結成功");
        } catch (error) {
          console.error("解除連結 Google 帳號失敗:", error);
          alert("解除連結 Google 帳號失敗，請稍後再試");
        }
      },
      async unlinkLine() {
        console.log("開始解除連結 Line 帳號");
        if (!this.canUnlinkLine) {
          alert("無法解除連結唯一的登入方式");
          return;
        }
        try {
          await this.unlinkSocialAccount("line");
          console.log("Line 帳號解除連結成功");
        } catch (error) {
          console.error("解除連結 Line 帳號失敗:", error);
          alert("解除連結 Line 帳號失敗，請稍後再試");
        }
      },
    },
    mounted() {
      console.log("user_setting 組件已掛載，認證狀態:", this.isAuthenticated);
      if (this.isAuthenticated) {
        this.loadUserSettings();
      } else {
        console.log("用戶未認證，重定向到登入頁面");
        this.$router.push("/login");
      }
    },
    watch: {
      user: {
        immediate: true,
        handler(newUser) {
          if (newUser) {
            console.log("用戶資料已更新:", newUser);
            this.loadUserSettings();
          }
        },
      },
      isAuthenticated(newValue) {
        console.log("認證狀態變更:", newValue);
        if (!newValue) {
          console.log("用戶已登出，重定向到登入頁面");
          this.$router.push("/login");
        }
      },
    },
  };
</script>
<style scoped>
  .user-setting {
    padding: 20px;
    max-width: 600px;
    margin: 0 auto;
    font-family: Arial, sans-serif;
  }

  .account-management,
  .personal-info {
    background-color: #f9f9f9;
    padding: 20px;
    border-radius: 8px;
    margin-bottom: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }

  h3 {
    margin-bottom: 15px;
    color: #333;
    font-size: 20px;
  }

  .linked-accounts {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  .unlink-button {
    width: 40%;
    margin-left: 10%;
    padding: 5px 10px;
    background-color: #ff6b6b;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 14px;
  }

  .unlink-button:hover {
    background-color: #ff4757;
  }

  .account-item {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 18px;
    color: #555;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
    transition: background-color 0.3s ease;
    cursor: pointer;
  }

  .account-item.linked {
    background-color: #e0f7fa;
  }

  .account-item:hover {
    background-color: #f1f1f1;
  }

  .form-group {
    margin-bottom: 20px;
  }

  label {
    display: block;
    margin-bottom: 5px;
    color: #666;
  }

  input {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 16px;
    color: #333;
    box-sizing: border-box;
  }

  button {
    width: 100%;
    padding: 12px;
    background-color: #d4b7a1;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 18px;
    cursor: pointer;
    margin-top: 20px;
    transition: background-color 0.3s ease;
  }

  button:hover {
    background-color: #b3957e;
  }

  .popup-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
  }

  .popup-content {
    background: white;
    padding: 30px;
    border-radius: 8px;
    text-align: center;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
  }
</style>
