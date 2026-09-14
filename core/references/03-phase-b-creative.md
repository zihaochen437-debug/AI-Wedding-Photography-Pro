# Phase B｜工作模式、产品、套系、Look 与 Scene

> v2.0.0 开发规则。仅当人物标准阶段 `9/9 APPROVED + FROZEN` 后进入。

## 1. PHASE_B_WORK_MODE_GATE

进入任何 Suite / Style / Look / Scene 规划之前，必须先让用户选择工作模式：

A. **Ai自动｜AI_AUTO**：Skill 主动分析需求并提出方案，在用户已经授予的范围内自动完成创意规划与执行；不自动取得故事或分镜自主权。

B. **自动｜PRESET_AUTO**：优先调用经过验证的商业预设和默认规划器，用户在关键阶段审核。

C. **半自动｜SEMI_AUTO**：推荐商业默认。用户决定主要方向，Skill 负责补齐妆造、Scene、道具、Shot 和技术细节并逐阶段确认。

D. **自定义｜CUSTOM**：用户对风格、服装、妆容、发型、道具、场景、摄影、视频等提出更细要求，Skill 负责专业化整理、冲突检查与执行编译。

硬规则：

- `WORK_MODE_DOES_NOT_BYPASS_QC`：任何模式不得跳过身份、人体、Look、Scene、摄影或视频 QC。
- 工作模式只决定默认决策权与交互密度，不自动等于 `STORY_AUTONOMY` 或 `STORYBOARD_AUTONOMY`。
- 用户随时可以从自动模式切换为更高人工控制，已批准资产继续有效，不得无故重做。

## 2. PROJECT_OUTPUT_TYPE_GATE

工作模式确认后再确定：

A. 只制作婚纱照片  
B. 只制作婚纱影视  
C. 照片 + 婚纱影视

有照片进入 `TARGET_PHOTO_COUNT_GATE`；有影视进入 `WEDDING_FILM_PRODUCT_CLASS`（VF01 / VF02 / VF03）。

## 3. PRODUCT_BRANCH_DEPENDENCY_ROUTER

Phase A 的 9 张身份资产是所有真人产品共同底座；但 Phase B 下游资产按产品需要创建，**不得为了流程完整而强制生成无用 Look/Scene**。

### PHOTO｜婚纱摄影

默认需要婚纱线：

`Suite/Style → AB04 bride Look → AB05 groom Look → Prop → AB06 Scene → DIR01 → Photo Shot`

如果某类照片本身不需要 Scene Master（例如用户以已批准实拍背景/完整样片作为唯一视觉母体），允许按当前任务建立更小的权威链，但必须记录理由和真实 Reference Binding。

### VF01｜动态婚纱影像

VF01 必须有 `WEDDING_PHOTO_SOURCE`，可以是：

- `PROJECT_APPROVED_WEDDING_PHOTO`：本项目已经批准的婚纱成片；
- `USER_SUPPLIED_WEDDING_PHOTO`：用户上传的既有婚纱照片，先登记、身份/内容 QC、确认可作为动态视觉母体，再升级为当前项目 Approved Source。

如果婚纱照片已经完整定义人物、Look、Scene 和构图，**不要求为了 VF01 再额外重建 AB04/AB05/AB06**。只有当需要补镜、换 Scene、重新设计 Look 或创建新婚纱镜头时，才创建对应婚纱资产。

### VF02｜创意叙事婚纱影视

纯 VF02 **不强制先做 AB04/AB05/AB06**。

从 AB01/AB02/AB03 身份根进入：

`Approved Story → Script Breakdown → STORY CHARACTER STATE / STORY LOOK / STORY WARDROBE / STORY PROP / FILM SCENE → VD01/VC01/VB01 → Shot`

剧情人物仍然是同一真人身份，但剧情 Look 可以是学生、旅行、日常、年代服装或任何用户/剧本需要的角色状态，不必先穿婚纱。

只有剧本中确实出现婚纱时期，才为对应段落创建婚纱 Look/Scene 或引用 Approved Wedding Photos。

### VF03｜混合叙事婚纱短片

VF03 必须同时具备：

1. `STORY_LINE_ASSETS`：Story Character State / Story Look / Story Props / Film Scenes；
2. `WEDDING_LINE_SOURCE`：以下至少一种：
   - Approved Wedding Photos；
   - 本项目 AB04/AB05 + AB06 + Wedding Shot；
   - 用户提供并经项目批准的婚纱影像素材。

两条线通过 Bridge Map、视觉母题、动作、道具、声音、色彩或时空关系连接，不要求重复生成已有有效婚纱资产。

### 照片 + 影视组合项目

共享所有实际相同的 Frozen 身份、婚纱 Look、Scene、道具和 Wedding Shot；影视剧情线再创建独立 Story Assets。不得因为进入视频分支重新设计已经批准的婚纱世界。

## 4. TARGET_PHOTO_COUNT_GATE

有照片时先问最终独立保留数量：6 / 9 / 12 / 18 / 24 / 36 / 48+ / 自定义 / AI推荐。不是候选数或生成次数。

软规划：6–9 以 1 个主要视觉方向为主；12–18 约 1–2 个方向/Look/Scene；24–36 可规划 2–3 个主要方向与多 Scene/Sequence；48+ 适合完整多套系。

这些是规划基线，不是硬公式；用户明确需要极简、单场景、固定机位或其他创意时允许有理由偏离。

## 5. BROAD_CHOICE_PRESENTATION_POLICY

用户“都有什么/多看看/没想好”进入 `FULL_CATALOG_MODE`；已有偏好进入 `RECOMMENDATION_MODE`，建议 6–10 个真正有跨度的方向，并始终提供更多同类、完整分类、自定义、上传参考。

能力范围包括但不限于：经典、韩式清透、法式轻奢、现代极简、高定影棚、Editorial、电影纪实、电影情绪、复古胶片、草坪、森林、海边、山野、花海、城市街拍、城市夜景、欧式建筑、法式室内、新中式、秀禾、龙凤褂、汉服、明制、宋制、民国、东方高定、旅行、艺术情绪、创意实验。

预设只是商业起点，不构成创作能力边界。用户上传的服装、妆容、发型、场景、姿势、灯光、构图、故事和自定义创意优先。

## 6. 多选与分支

Suite / Style / Look / Scene / 产品比例可多选，但默认建立独立 `SUITE-0N` 分支，不把所有方向塞进一个 Prompt。用户明确要求“融合”时才建立受控复合风格。

## 7. WEDDING LOOK CHAIN

只有当前产品/段落需要婚纱线时才执行：

`SUITE → STYLE → BRIDE LOOK PLAN → AB04 → GROOM LOOK PLAN → AB05 → LOOK REVIEW → PROP → SCENE PLAN → AB06 → DIRECTOR / BLOCKING / CAMERA / STORYBOARD`

AB04/AB05 分别审核冻结后才可把 Wedding Look 阶段视为完成；AB06 建立前确认当前 Look 与 Scene 在时代、色彩、材质和使用场景上兼容。

## 8. LOOK_NAME_IS_NOT_GENERATION_PROMPT

“法式清透”“韩式”“新中式”“高定”“电影纪实”等只能作为用户 UI / 方案名称，必须经过 `LOOK_PROFILE_RESOLVER` 展开，不能把一个风格标签直接当成正式生成 Prompt。

### 新娘 Look Resolver

至少解析：

`identity_anchor / makeup / hair / dress / fabric / silhouette / neckline / sleeves / waist / skirt_train / veil / headpiece / earrings / necklace / shoes / visible_jewelry / personal_signatures / forbidden_changes`

### 新郎 Look Resolver

至少解析：

`identity_anchor / grooming / hair / suit_or_costume / shoulder_line / lapel_or_collar / shirt / tie_or_bow / waistcoat_or_cummerbund / cufflinks / trousers / shoes / boutonniere / watch_ring / fabric / personal_signatures / forbidden_changes`

Story Look 使用相同 Resolver 思想，但字段根据剧情角色状态裁剪，不默认加入婚纱/头纱/胸花等婚礼元素。

## 9. BRIDE_MAKEUP_REQUIRED / EXPLICIT_MAKEUP_COMPILATION

任何需要正式新娘 Wedding Look 的 AB04 首版必须明确存在可执行妆面描述，除非用户明确选择“无妆/极近原貌妆”。不能只写“精致新娘妆”“法式妆容”等空标签。

妆面至少解析：

`base_and_complexion / skin_finish / brows / eyeshadow / eyeliner / lashes / under_eye / blush / contour / highlight / lips / intensity / texture_retention`

执行原则：

- 妆容只能改变化妆可改变的可见状态，不擅自改变真实脸型、眼距、鼻形、嘴形、下颌或年龄身份；
- 保留真实皮肤纹理，不用厚磨皮制造“妆”；
- 用户已冻结的 Retouch Profile 继续作为皮肤/人物基线，Makeup Resolver 在其上增加化妆状态，而不是再次美容；
- 传统/年代/文化妆面需要与服装、发型、饰品和 Scene 保持一致。

## 10. LOOK_PROMPT_PREFLIGHT

提交正式 Wedding Look 或 Story Look 生成前检查：

- 是否真实绑定 M01 及必要 U/F/D 身份资产；
- 是否解析用户选择的 Look，而不是只发送名称；
- 需要妆容时是否包含可见、可执行的眉眼、唇、肤质和强度信息；
- 发型、头饰/头纱、饰品与服装结构是否相互冲突；
- 是否保留用户个人标志；
- 是否存在未经授权的年轻化、瘦脸、体型改变或五官重设计；
- Prompt 是否只保留当前任务必要信息，避免参考与文字互相打架。

未通过则 `LOOK_GENERATION_BLOCKED`。

## 11. MAKEUP_PRESENCE_GATE / LOOK_IDENTITY_GATE

Look 审核分别判断：

1. **Identity Fidelity**：仍然能明确识别为同一人物；
2. **Makeup Presence & Accuracy**：需要妆面时，批准妆容确实存在且强度正确；
3. **Hair / Wardrobe / Accessory**：发型、服装和饰品结构正确；
4. **Editability**：后续局部改妆/改发型能否在不破坏身份和服装的情况下执行。

“脸像但几乎没执行批准妆容”和“妆容漂亮但已经不像本人”都不能通过。

## 12. LOOK_EDIT_FIRST / MAKEUP_REVISION_SCOPE_LOCK

Look 某一域不合格时优先在当前已正确版本上做局部编辑，不默认重生整张。

例如只调整眼妆：只开放眼影、眼线、睫毛和必要连接区域；冻结脸型、其他五官、另一人物、发型、服装、饰品、Scene、Camera 与已经正确的肤质。

修改妆容后再次执行 `LOOK_IDENTITY_GATE`，避免出现 `MAKEUP_IDENTITY_DRIFT`。

## 13. 商业能力目录

### 新娘 / 女性角色
妆面、发型、婚纱/剧情服装轮廓、领口、袖型、腰线、裙摆/拖尾、面料、蕾丝/刺绣/珠饰、头纱、头饰、耳饰、项链、鞋履等，且包括但不限于这些预设。

### 新郎 / 男性角色
面部整理、发型、西装/礼服/剧情服装版型、肩线、翻领/立领、衬衫、领带/领结、马甲/腰封、袖扣、裤型、鞋履、胸花、手表/戒指、面料与配色，且允许任何剧情或用户自定义服装体系。

### 道具
花束、团扇、伞、茶具、香槟杯、书、乐器、车辆、宠物、家具、纪念物等；记录谁拿、哪只手、握持点、高度、方向、状态变化和另一只手状态。清单包括但不限于这些示例。

### 传统与历史风格
服装、妆发、饰品、道具和 Scene 需要时代/文化一致性；用户自有服装和自定义参考优先。