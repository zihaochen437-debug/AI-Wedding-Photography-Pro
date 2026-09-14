# Phase B｜工作模式、产品、套系、Look 与 Scene

> v2.0.0 开发规则。仅当人物标准阶段 `9/9 APPROVED + FROZEN` 后进入。

## 1. PHASE_B_WORK_MODE_GATE

进入任何创意规划前先选择：

A. **Ai自动｜AI_AUTO**：Skill 在用户已授权范围内主动规划；不自动取得故事或分镜自主权。  
B. **自动｜PRESET_AUTO**：优先使用经过验证的商业预设与默认规划器，关键阶段用户审核。  
C. **半自动｜SEMI_AUTO**：推荐商业默认；用户决定主要方向，Skill 补齐专业细节。  
D. **自定义｜CUSTOM**：用户给出更细创意，Skill 负责专业化整理、冲突检查与执行编译。

`WORK_MODE_DOES_NOT_BYPASS_QC`。工作模式不自动改变 `STORY_AUTONOMY / STORYBOARD_AUTONOMY`。

## 2. PROJECT_OUTPUT_TYPE_GATE

工作模式确认后确定：

A. 婚纱照片  
B. 婚纱影视  
C. 照片 + 婚纱影视

有照片进入 `TARGET_PHOTO_COUNT_GATE`；有影视进入 `WEDDING_FILM_PRODUCT_CLASS`（VF01 / VF02 / VF03）。

## 3. PRODUCT_BRANCH_DEPENDENCY_ROUTER

Phase A 九图身份标准是共同底座；Phase B 下游资产按真实产品需求创建，**不得为了流程完整强制生产无用婚纱 Look 或 Scene**。

### PHOTO

默认婚纱线：

`Suite/Style → AB04 bride Look → AB05 groom Look → Prop → AB06 Scene → DIR01 → Photo Shot`

如果当前 Shot 已由用户批准的完整视觉母体定义，可建立更小的权威链，但必须记录来源、职责和 Reference Binding。

### VF01｜动态婚纱影像

必须有 `WEDDING_PHOTO_SOURCE`：

- `PROJECT_APPROVED_WEDDING_PHOTO`；或
- `USER_SUPPLIED_WEDDING_PHOTO`：先登记、身份/内容 QC 并经用户确认成为 Approved Source。

如果源照片已经完整定义身份、Look、Scene 和构图，不要求为了 VF01 重建 AB04/AB05/AB06。只有补镜、换 Scene、重设计 Look 或新增婚纱 Shot 时才创建对应资产。

### VF02｜创意叙事婚纱影视

纯 VF02 **不强制先做 AB04/AB05/AB06**。

从九图身份根进入：

`Approved Story → Script Breakdown → STORY CHARACTER STATE / STORY LOOK / STORY WARDROBE / STORY PROP / FILM SCENE → VD01/VC01/VB01 → Shot`

剧情 Look 可以是学生、旅行、日常、年代服装或任何用户/剧本需要的角色状态。只有剧本出现婚纱时期，才创建婚纱 Look/Scene 或引用 Approved Wedding Photos。

### VF03｜混合叙事婚纱短片

必须同时具备：

1. `STORY_LINE_ASSETS`：Story Character State / Story Look / Story Props / Film Scenes；
2. `WEDDING_LINE_SOURCE` 至少一种：Approved Wedding Photos；本项目 AB04/AB05+AB06+Wedding Shot；或用户提供并经项目批准的婚纱影像素材。

两线通过 Bridge Map、视觉母题、动作、道具、声音、色彩或时空关系连接，不重复生成已有有效婚纱资产。

### 照片 + 影视组合

共享实际相同的 Frozen 身份、婚纱 Look、Scene、道具和 Wedding Shot；剧情线另建 Story Assets。不得进入视频分支后重新设计已批准婚纱世界。

## 4. TARGET_PHOTO_COUNT_GATE

最终独立保留照片数量：6 / 9 / 12 / 18 / 24 / 36 / 48+ / 自定义 / AI 推荐。

软规划：6–9 约 1 个主视觉方向；12–18 约 1–2 个 Look/Scene；24–36 约 2–3 个主要方向；48+ 适合完整多套系。它不是硬公式，极简、固定机位或用户明确创意允许合理偏离。

## 5. BROAD_CHOICE_PRESENTATION_POLICY

用户说“全部/都有什么/没想好”进入 `FULL_CATALOG_MODE`；已有偏好进入 `RECOMMENDATION_MODE`，推荐 6–10 个有真正跨度的方向，并始终保留完整分类、自定义、上传参考。

能力包括但不限于经典、韩式、法式、现代极简、高定影棚、Editorial、电影纪实/情绪、胶片、自然外景、城市、建筑、新中式、传统婚服、历史服饰、旅行、艺术实验等。预设不是能力边界。

## 6. 多选与独立分支

Suite / Style / Look / Scene / 产品比例可多选，但默认建立独立 `SUITE-0N` 分支。只有用户明确“融合”时才建立复合方向。

## 7. WEDDING LOOK CHAIN

只有当前产品/段落需要婚纱线时执行：

`SUITE → STYLE → BRIDE LOOK PLAN → AB04 → GROOM LOOK PLAN → AB05 → LOOK REVIEW → PROP → SCENE PLAN → AB06 → DIRECTOR/BLOCKING/CAMERA/STORYBOARD`

AB04/AB05 分别审核冻结后才算 Wedding Look 完成；AB06 与 Look 必须在时代、色彩、材质和场景用途上兼容。

## 8. LOOK_NAME_IS_NOT_GENERATION_PROMPT

“法式清透”“韩式”“新中式”“高定”“电影纪实”等只是 UI/方案名，必须经过 `LOOK_PROFILE_RESOLVER`。

新娘至少解析：`identity_anchor / makeup / hair / dress / fabric / silhouette / neckline / sleeves / waist / skirt_train / veil / headpiece / earrings / necklace / shoes / visible_jewelry / personal_signatures / forbidden_changes`。

新郎至少解析：`identity_anchor / grooming / hair / suit_or_costume / shoulder_line / lapel_or_collar / shirt / tie_or_bow / waistcoat_or_cummerbund / cufflinks / trousers / shoes / boutonniere / watch_ring / fabric / personal_signatures / forbidden_changes`。

Story Look 使用相同思想，但按剧情裁剪，不默认加入婚纱/头纱/胸花。

## 9. BRIDE_MAKEUP_REQUIRED / EXPLICIT_MAKEUP_COMPILATION

需要 Wedding Bride Look 时，除用户明确无妆/极近原貌妆，首版必须明确：

`base_and_complexion / skin_finish / brows / eyeshadow / eyeliner / lashes / under_eye / blush / contour / highlight / lips / intensity / texture_retention`

妆容只能改变真实化妆可改变的可见状态，不擅自改变脸型、眼距、鼻形、嘴形、下颌、年龄或身份。Retouch Profile 是皮肤/人物基线，Makeup Resolver 在其上增加化妆状态，不再次美容。

## 10. LOOK_PROMPT_PREFLIGHT

正式 Wedding Look 或 Story Look 生成前检查：身份 M01/U/F/D 绑定、Look 是否已解析、需要妆容时眉眼唇/肤质/强度是否明确、发型/头饰/服装是否冲突、个人标志是否正确、是否存在未经授权的年轻化/瘦脸/体型/五官重设计。

未通过：`LOOK_GENERATION_BLOCKED`。

## 11. MAKEUP_PRESENCE_GATE / LOOK_IDENTITY_GATE

分别判断：

1. Identity Fidelity；
2. Makeup Presence & Accuracy（适用时）；
3. Hair / Wardrobe / Accessory；
4. Editability。

“脸像但没执行批准妆容”和“妆容漂亮但不像本人”都不能通过。

## 12. LOOK_EDIT_FIRST / MAKEUP_REVISION_SCOPE_LOCK

局部问题优先编辑当前正确版本，不默认重生整张。例如只改眼妆，只开放眼影、眼线、睫毛和必要连接区域；锁定其他已批准域。改后再次执行 `LOOK_IDENTITY_GATE`。

## 13. 商业资产开放原则

人物造型、服装、道具、Scene、宠物、历史/传统元素、剧情角色状态等均**包括但不限于**现有示例。剧本和用户创意可以动态提出新资产，经专业检查和用户审核后进入项目。