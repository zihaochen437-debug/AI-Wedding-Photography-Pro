# AB01–AB06｜v2 资产权威、九图标准人物与状态依赖

## 1. 六个逻辑核心资产，不等于六张图片

v2 继续保留 AB01–AB06 的逻辑职责，但取消 v1 中“AB01–AB06 等于六张物理图片”的旧解释：

- **AB01**｜新娘标准人物资产包
- **AB02**｜新郎标准人物资产包
- **AB03**｜双人正面全身比例母版
- **AB04**｜新娘 Final Look Master
- **AB05**｜新郎 Final Look Master
- **AB06**｜Scene Master

AB01/AB02 是逻辑资产包，各包含 4 张正式人物标准输出；AB03 只有 1 张正式双人标准照。人物标准阶段总计 `4 + 4 + 1 = 9 images`。

AB04/AB05 并排协调只是临时 Review View，不成为新的身份权威。

## 2. STANDARD_IDENTITY_4_PLUS_1_POLICY

### AB01｜新娘

- `AB01-M01 / FRONT_MEDIUM_MASTER`｜正面中景标准照
- `AB01-U01 / UPPER_BODY_STANDARD_BOARD`｜上半身标准资产板
- `AB01-F01 / FULL_BODY_STANDARD_BOARD`｜全身标准资产板
- `AB01-D01 / DETAIL_STANDARD_BOARD`｜人物特写细节资产板

### AB02｜新郎

- `AB02-M01 / FRONT_MEDIUM_MASTER`
- `AB02-U01 / UPPER_BODY_STANDARD_BOARD`
- `AB02-F01 / FULL_BODY_STANDARD_BOARD`
- `AB02-D01 / DETAIL_STANDARD_BOARD`

### AB03｜双人

- `AB03-C01 / COUPLE_FRONT_FULL_BODY_MASTER`｜唯一双人正面全身标准照

只有以上 9 个物理输出属于人物标准阶段正式槽位。不得新增“左45标准照”“右侧面标准照”“背面标准照”等额外正式槽位。

## 3. 板内多视角不是独立权威资产

U/F/D 资产板可以包含当前任务需要的多视角/细节区域，但：

- 板内区域不单独注册为正式人物权威资产；
- 不得因某一角度需要参考就新增第 5 张单人人物标准图；
- 标准制作优先把多视角集中在对应 U/F/D 一张正式板中；
- 若小云雀当前模型稳定性需要临时中间图，它们只能标记 `WORKING_ARTIFACT`，不得进入正式 9 图槽位，也不得绕过用户审核成为权威；
- 板内一区域失败时冻结其他正确区域，仅修失败区域并输出同一槽位的新版本。

## 4. FRONT_MEDIUM_MASTER 是单人人物最高身份锚

M01 负责真实脸型、五官比例、年龄感、发际线、肤色、面部体量、精修基线与个人标志。

U/F/D 必须直接继承已 `APPROVED + FROZEN` 的 M01，不得分别从原始照片重新“造一个同人”。原始角度参考仅用于补充 M01 看不到的真实结构。

## 5. UPPER_BODY_STANDARD_BOARD

负责头肩、上半身与必要多观察方向的一致性。可包含正面、左右45、左右侧面、背面头肩/上半身以及必要耳形、发际线等区域。

所有区域必须属于同一个已批准人物，并保持完全一致的精修状态、肤色、年龄、标准服装和中性光。

## 6. FULL_BODY_STANDARD_BOARD

负责真实体型、头身比、肩宽、躯干、四肢、手、腿、鞋底基准与身体方向。必要多方向集中在同一 F01 正式板内。

`HEAD_VIEW_DIRECTION` 与 `BODY_ORIENTATION` 分离。左45/右45按画面方向解释，身体方向主要由胸骨/躯干轴确定；禁止水平镜像伪造真实另一侧。

## 7. DETAIL_STANDARD_BOARD

按任务区域组织眼/眉、鼻、唇/牙、耳、发际线、头发/胡须、双手及用户独有特征。

细节板只强化真实存在且有依据的特征；看不到的区域保持 `UNKNOWN/UNCERTAIN`，不得把 AI 推演结果反写成用户真实证据。

## 8. AB03-C01｜唯一双人正面全身标准照

AB03 只负责双人共存、真实比例和尺度校准，不再建立双人六方向资产板。

要求：同一平整地面、同一前后平面、自然间距、正面全身完整入镜、不拥抱、不牵手、不贴脸；核对相对头部大小、头顶高度、眼位、肩线、身体宽度、真实身高差、头身比、手部和鞋底基准。

身份权威关系：AB01-M01/AB02-M01 的面部身份高于 AB03；AB03 的双人身高、体型与同框比例高于单人图的相对推测。

## 9. 输出规格真实性

资产输出竖向优先、2:3 优先、sRGB；固定 8000×12000、8K/12K、一亿像素母版全部废弃。

记录：`REQUESTED_QUALITY / REQUESTED_RATIO / REQUESTED_SIZE / ACTUAL_NATIVE_SIZE / UPSCALE_USED / FINAL_OUTPUT_SIZE`。

4K 是当前平台质量/请求档位概念，不是固定像素尺寸；人物正确性 > 像素档位。

## 10. NEUTRAL_ASSET_CAPTURE_LOCK

AB01–AB05、独立人物/服装/道具资产：

- `#FFFFFF` 纯白无缝背景
- 自然中性柔和面光
- 低反差、中性白平衡、准确曝光
- 真实肤色与材质
- 禁止蓝/红/紫/暖黄染色、霓虹、强侧光、强逆光、戏剧轮廓光、渐变/灰/米黄艺术背景

AB06 Scene Base 保留真实 Scene，但使用自然中性基准光建立空间、颜色和材质。黄金时刻、蓝调、夜景、电影侧光等只进入正式 Photo/Video Shot。

原则：**先真实建档，再创意拍摄。**

## 11. AB04 / AB05

Final Look Master。身份锚必须直接复用 AB01-M01 / AB02-M01 及必要 U/F/D 已冻结内容，不重新生成“像”的锚点。

负责妆容、发型、婚纱/礼服、面料、鞋履、穿戴配饰、头纱、珠宝、男士领饰、袖扣、胸花等；男女深度对等。

花束、伞、团扇等具体 Shot 道具原则上保持独立。

## 12. AB06

默认无新娘、新郎、陌生模特。记录 Scene ID、地面、建筑、道路、门窗、植物、家具、花艺、固定装置、主要材质、前/中/后景、安全站立区、遮挡、Outpaint 边界、兼容 Look/Props。

多视图执行 `Same World, Different Camera`：换摄影机，不换世界。

## 13. 状态机与槽位版本

统一状态：`DRAFT / UNDER_USER_REVIEW / REVISION_REQUIRED / APPROVED / FROZEN / SUPERSEDED / REJECTED / QUARANTINE`。

只有 `APPROVED + FROZEN` 可作为正式下游权威。REJECTED/QUARANTINE 禁止继续引用。

同一正式槽位修订采用版本替换，例如 `AB01-U01-V01 → SUPERSEDED`、`AB01-U01-V02 → APPROVED + FROZEN`；不得通过新增 U02/U03 逃避修订。

## 14. 资产依赖与失效传播

`RAW REFERENCES → Retouch Profile + Standard Wardrobe → AB01/AB02 M/U/F/D → AB03-C01 → AB04/AB05 → AB06 → Blocking/Storyboard/Camera/Lighting → Photo/Video Shot → Approved Baseline → Derived Outputs`

上游变化按实际依赖标记：`VALID / NEEDS_REVALIDATION / INVALIDATED / SUPERSEDED`。

不要无脑全项目重做：人物 M01 更新会使该人物 U/F/D、相关 Look 与下游 Shot 进入复核；AB06 只影响使用该 Scene 的内容；纯输出尺寸变化通常不要求重新生人物。